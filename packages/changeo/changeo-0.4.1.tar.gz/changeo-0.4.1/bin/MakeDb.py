#!/usr/bin/env python3
"""
Create tab-delimited database file to store sequence alignment information
"""

# Info
__author__ = 'Namita Gupta, Jason Anthony Vander Heiden'
from changeo import __version__, __date__

# Imports
import os
import re
import sys
from argparse import ArgumentParser
from collections import OrderedDict
from textwrap import dedent
from time import time
from Bio import SeqIO

# Presto and changeo imports
from presto.Annotation import parseAnnotation
from presto.IO import countSeqFile, printLog, printMessage, printProgress, readSeqFile
from changeo.Defaults import default_format, default_out_args
from changeo.Commandline import CommonHelpFormatter, checkArgs, getCommonArgParser, parseCommonArgs
from changeo.Gene import buildGermline
from changeo.IO import countDbFile, extractIMGT, readGermlines, getFormatOperators, getOutputHandle, \
                       AIRRWriter, ChangeoWriter, IgBLASTReader, IMGTReader, IHMMuneReader
from changeo.Receptor import ChangeoSchema, AIRRSchema


def addGermline(receptor, references):
    """
    Add full length germline to Receptor object

    Arguments:
      receptor (changeo.Receptor.Receptor): Receptor object to modify.
      references (dict): dictionary of IMGT-gapped references sequences.

    Returns:
      changeo.Receptor.Receptor: modified Receptor with the germline_imgt attribute added.
    """
    __, germlines, __ = buildGermline(receptor, references)
    germline_seq = None if germlines is None else germlines['full']
    receptor.setField('germline_imgt', germline_seq)

    return receptor


def getIDforIMGT(seq_file):
    """
    Create a sequence ID translation using IMGT truncation.

    Arguments:
      seq_file : a fasta file of sequences input to IMGT.

    Returns:
      dict : a dictionary of with the IMGT truncated ID as the key and the full sequence description as the value.
    """

    # Create a sequence ID translation using IDs truncate up to space or 50 chars
    ids = {}
    for rec in readSeqFile(seq_file):
        if len(rec.description) <= 50:
            id_key = rec.description
        else:
            id_key = re.sub('\||\s|!|&|\*|<|>|\?', '_', rec.description[:50])
        ids.update({id_key: rec.description})

    return ids


def getSeqDict(seq_file):
    """
    Create a dictionary from a sequence file.

    Arguments:
      seq_file : sequence file.

    Returns:
        dict : sequence description as keys with Bio.SeqRecords as values.
    """
    seq_dict = SeqIO.to_dict(readSeqFile(seq_file), key_function=lambda x: x.description)

    return seq_dict


def writeDb(records, fields, aligner_file, total_count, id_dict=None, partial=False, asis_id=True,
            writer=ChangeoWriter, out_file=None, out_args=default_out_args):
    """
    Writes tab-delimited database file in output directory.
    
    Arguments:
      records : a iterator of Receptor objects containing alignment data.
      fields : a list of ordered field names to write.
      aligner_file : input file name.
      total_count : number of records (for progress bar).
      id_dict : a dictionary of the truncated sequence ID mapped to the full sequence ID.
      partial : if True put incomplete alignments in the pass file.
      asis_id : if ID is to be parsed for pRESTO output with default delimiters.
      writer : writer class.
      out_file : output file name. Automatically generated from the input file if None.
      out_args : common output argument dictionary from parseCommonArgs.

    Returns:
      None
    """
    # Wrapper for opening handles and writers
    def _open(x, fields=fields, writer=writer, out_file=out_file):
        if out_file is not None and x == 'pass':
            handle = open(out_file, 'w')
        else:
            handle = getOutputHandle(aligner_file,
                                     out_label='db-%s' % x,
                                     out_dir=out_args['out_dir'],
                                     out_name=out_args['out_name'],
                                     out_type=out_args['out_type'])
        return handle, writer(handle, fields=fields)

    # Function to convert fasta header annotations to changeo columns
    def _changeo(fields, header):
        f = [ChangeoSchema.fromReceptor(x) for x in header if x.upper() not in fields]
        fields.extend(f)
        return fields

    def _airr(fields, header):
        f = [AIRRSchema.fromReceptor(x) for x in header if x.lower() not in fields]
        fields.extend(f)
        return fields

    # Function to check for valid records strictly
    def _strict(rec):
        valid = [rec.v_call and rec.v_call != 'None',
                 rec.j_call and rec.j_call != 'None',
                 rec.functional is not None,
                 rec.sequence_imgt,
                 rec.junction]
        try:  imgt_check = (rec.junction == rec.sequence_imgt[309:(309 + rec.junction_length)])
        except TypeError:  imgt_check = False
        return all(valid) and imgt_check

    # Function to check for valid records loosely
    def _gentle(rec):
        valid = [rec.v_call and rec.v_call != 'None',
                 rec.d_call and rec.d_call != 'None',
                 rec.j_call and rec.j_call != 'None']
        return any(valid)

    # Set writer class and annotation conversion function
    if writer == ChangeoWriter:
        _annotate = _changeo
    elif writer == AIRRWriter:
        _annotate = _airr
    else:
        sys.exit('Invalid output writer')

    # Set pass criteria
    _pass = _gentle if partial else _strict

    # Initialize handles, writers and counters
    pass_handle, pass_writer = None, None
    fail_handle, fail_writer = None, None
    pass_count, fail_count = 0, 0
    start_time = time()

    # Validate and write output
    printProgress(0, total_count, 0.05, start_time)
    for i, record in enumerate(records, start=1):
        # Replace sequence description with full string, if required
        if id_dict is not None and record.sequence_id in id_dict:
            record.sequence_id = id_dict[record.sequence_id]

        # Parse sequence description into new columns
        if not asis_id:
            try:
                ann_raw = parseAnnotation(record.sequence_id)
                record.sequence_id = ann_raw.pop('ID')

                # Convert to Receptor fields
                ann_parsed = OrderedDict()
                for k, v in ann_raw.items():
                    ann_parsed[ChangeoSchema.toReceptor(k)] = v

                # If first record, use parsed description to define extra columns
                if i == 1:  fields = _annotate(fields, ann_parsed.keys())

                # Update Receptor record
                record.setDict(ann_parsed, parse=True)
            except IndexError:
                # Could not parse pRESTO-style annotations so fall back to no parse
                asis_id = True
                sys.stderr.write('\nWARNING: Sequence annotation format not recognized. Sequence headers will not be parsed.\n')

        # Count pass or fail and write to appropriate file
        if _pass(record):
            pass_count += 1
            # Write row to pass file
            try:
                pass_writer.writeReceptor(record)
            except AttributeError:
                # Open pass file and writer
                pass_handle, pass_writer = _open('pass')
                pass_writer.writeReceptor(record)

        else:
            fail_count += 1
            # Write row to fail file if specified
            if out_args['failed']:
                try:
                    fail_writer.writeReceptor(record)
                except AttributeError:
                    # Open fail file and writer
                    fail_handle, fail_writer = _open('fail')
                    fail_writer.writeReceptor(record)

        # Print progress
        printProgress(i, total_count, 0.05, start_time)

    # Print consol log
    log = OrderedDict()
    log['OUTPUT'] = os.path.basename(pass_handle.name) if pass_handle is not None else None
    log['PASS'] = pass_count
    log['FAIL'] = fail_count
    log['END'] = 'MakeDb'
    printLog(log)

    # Close file handles
    output = {'pass': None, 'fail': None}
    if pass_handle is not None:
        output['pass'] = pass_handle.name
        pass_handle.close()
    if fail_handle is not None:
        output['fail'] = fail_handle.name
        fail_handle.close()

    return output


# TODO:  may be able to merge with other mains
def parseIMGT(aligner_file, seq_file=None, repo=None, partial=False, asis_id=True,
              parse_scores=False, parse_regions=False, parse_junction=False,
              format=default_format, out_file=None, out_args=default_out_args):
    """
    Main for IMGT aligned sample sequences.

    Arguments:
      aligner_file : zipped file or unzipped folder output by IMGT.
      seq_file : FASTA file input to IMGT (from which to get seqID).
      repo : folder with germline repertoire files.
      partial : If True put incomplete alignments in the pass file.
      asis_id : if ID is to be parsed for pRESTO output with default delimiters.
      parse_scores : if True add alignment score fields to output file.
      parse_regions : if True add FWR and CDR region fields to output file.
      format : output format. one of 'changeo' or 'airr'.
      out_file : output file name. Automatically generated from the input file if None.
      out_args : common output argument dictionary from parseCommonArgs.

    Returns:
      dict : names of the 'pass' and 'fail' output files.
    """
    # Print parameter info
    log = OrderedDict()
    log['START'] = 'MakeDb'
    log['ALIGNER'] = 'IMGT'
    log['ALIGNER_FILE'] = aligner_file
    log['SEQ_FILE'] = os.path.basename(seq_file) if seq_file else ''
    log['ASIS_ID'] = asis_id
    log['PARTIAL'] = partial
    log['SCORES'] = parse_scores
    log['REGIONS'] = parse_regions
    log['JUNCTION'] = parse_junction
    printLog(log)

    start_time = time()
    printMessage('Loading files', start_time=start_time, width=20)
    # Extract IMGT files
    temp_dir, imgt_files = extractIMGT(aligner_file)
    # Count records in IMGT files
    total_count = countDbFile(imgt_files['summary'])
    # Get (parsed) IDs from fasta file submitted to IMGT
    id_dict = getIDforIMGT(seq_file) if seq_file else {}
    printMessage('Done', start_time=start_time, end=True, width=20)

    # Define format operators
    try:
        __, writer, schema = getFormatOperators(format)
    except ValueError:
        sys.exit('Error:  Invalid format %s' % format)
    out_args['out_type'] = schema.out_type

    # Define output fields
    fields = list(schema.standard_fields)
    custom = IMGTReader.customFields(scores=parse_scores, regions=parse_regions,
                                     junction=parse_junction, schema=schema)
    fields.extend(custom)

    # Parse IMGT output and write db
    with open(imgt_files['summary'], 'r') as summary_handle, \
            open(imgt_files['gapped'], 'r') as gapped_handle, \
            open(imgt_files['ntseq'], 'r') as ntseq_handle, \
            open(imgt_files['junction'], 'r') as junction_handle:

        # Open parser
        parse_iter = IMGTReader(summary_handle, gapped_handle, ntseq_handle, junction_handle)

        # Add germline sequence
        if repo is None:
            germ_iter = parse_iter
        else:
            references = readGermlines(repo)
            germ_iter = (addGermline(x, references) for x in parse_iter)

        # Write db
        output = writeDb(germ_iter, fields=fields, aligner_file=aligner_file, total_count=total_count,
                         id_dict=id_dict, asis_id=asis_id, partial=partial,
                         writer=writer, out_file=out_file, out_args=out_args)

    # Cleanup temp directory
    temp_dir.cleanup()

    return output


# TODO:  may be able to merge with other mains
def parseIgBLAST(aligner_file, seq_file, repo, partial=False, asis_id=True, asis_calls=False,
                 parse_regions=False, parse_scores=False, parse_igblast_cdr3=False,
                 format='changeo', out_file=None, out_args=default_out_args):
    """
    Main for IgBLAST aligned sample sequences.

    Arguments:
      aligner_file : IgBLAST output file to process.
      seq_file : fasta file input to IgBlast (from which to get sequence).
      repo : folder with germline repertoire files.
      partial : If True put incomplete alignments in the pass file.
      asis_id : if ID is to be parsed for pRESTO output with default delimiters.
      asis_calls : if True do not parse gene calls for allele names.
      parse_regions : if True add FWR and CDR fields to output file.
      parse_scores : if True add alignment score fields to output file.
      parse_igblast_cdr3 : if True parse CDR3 sequences generated by IgBLAST.
      format : output format. one of 'changeo' or 'airr'.
      out_file : output file name. Automatically generated from the input file if None.
      out_args : common output argument dictionary from parseCommonArgs.

    Returns:
      dict : names of the 'pass' and 'fail' output files.
    """
    # Print parameter info
    log = OrderedDict()
    log['START'] = 'MakeDB'
    log['ALIGNER'] = 'IgBLAST'
    log['ALIGNER_FILE'] = os.path.basename(aligner_file)
    log['SEQ_FILE'] = os.path.basename(seq_file)
    log['PARTIAL'] = partial
    log['SCORES'] = parse_scores
    log['REGIONS'] = parse_regions
    log['ASIS_ID'] = asis_id
    log['ASIS_CALLS'] = asis_calls
    printLog(log)

    start_time = time()
    printMessage('Loading files', start_time=start_time, width=20)
    # Count records in sequence file
    total_count = countSeqFile(seq_file)
    # Get input sequence dictionary
    seq_dict = getSeqDict(seq_file)
    # Create germline repo dictionary
    references = readGermlines(repo, asis=asis_calls)
    printMessage('Done', start_time=start_time, end=True, width=20)

    # Define format operators
    try:
        __, writer, schema = getFormatOperators(format)
    except ValueError:
        sys.exit('Error:  Invalid format %s' % format)
    out_args['out_type'] = schema.out_type

    # Define output fields
    fields = list(schema.standard_fields)
    custom = IgBLASTReader.customFields(scores=parse_scores, regions=parse_regions,
                                        cdr3=parse_igblast_cdr3, schema=schema)
    fields.extend(custom)

    # Parse and write output
    with open(aligner_file, 'r') as f:
        parse_iter = IgBLASTReader(f, seq_dict, references, asis_calls=asis_calls)
        germ_iter = (addGermline(x, references) for x in parse_iter)
        output = writeDb(germ_iter, fields=fields, aligner_file=aligner_file, total_count=total_count,
                         partial=partial, asis_id=asis_id,
                         writer=writer, out_file=out_file, out_args=out_args)

    return output


# TODO:  may be able to merge with other mains
def parseIHMM(aligner_file, seq_file, repo, partial=False, asis_id=True,
              parse_scores=False, parse_regions=False,
              format=default_format, out_file=None, out_args=default_out_args):
    """
    Main for iHMMuneAlign aligned sample sequences.

    Arguments:
      aligner_file : iHMMune-Align output file to process.
      seq_file : fasta file input to iHMMuneAlign (from which to get sequence).
      repo : folder with germline repertoire files.
      partial : If True put incomplete alignments in the pass file.
      parse_scores : if True parse alignment scores.
      parse_regions : if True add FWR and CDR region fields.
      asis_id : if ID is to be parsed for pRESTO output with default delimiters.
      format : output format. One of 'changeo' or 'airr'.
      out_file : output file name. Automatically generated from the input file if None.
      out_args : common output argument dictionary from parseCommonArgs.

    Returns:
      dict : names of the 'pass' and 'fail' output files.
    """
    # Print parameter info
    log = OrderedDict()
    log['START'] = 'MakeDB'
    log['ALIGNER'] = 'iHMMune-Align'
    log['ALIGNER_FILE'] = os.path.basename(aligner_file)
    log['SEQ_FILE'] = os.path.basename(seq_file)
    log['ASIS_ID'] = asis_id
    log['PARTIAL'] = partial
    log['SCORES'] = parse_scores
    log['REGIONS'] = parse_regions
    printLog(log)

    start_time = time()
    printMessage('Loading files', start_time=start_time, width=20)
    # Count records in sequence file
    total_count = countSeqFile(seq_file)
    # Get input sequence dictionary
    seq_dict = getSeqDict(seq_file)
    # Create germline repo dictionary
    references = readGermlines(repo)
    printMessage('Done', start_time=start_time, end=True, width=20)

    # Define format operators
    try:
        __, writer, schema = getFormatOperators(format)
    except ValueError:
        sys.exit('Error:  Invalid format %s' % format)
    out_args['out_type'] = schema.out_type

    # Define output fields
    fields = list(schema.standard_fields)
    custom = IHMMuneReader.customFields(scores=parse_scores, regions=parse_regions,
                                        schema=schema)
    fields.extend(custom)

    # Parse and write output
    with open(aligner_file, 'r') as f:
        parse_iter = IHMMuneReader(f, seq_dict, references)
        germ_iter = (addGermline(x, references) for x in parse_iter)
        output = writeDb(germ_iter, fields=fields, aligner_file=aligner_file, total_count=total_count,
                         asis_id=asis_id, partial=partial,
                         writer=writer, out_file=out_file, out_args=out_args)

    return output


def getArgParser():
    """
    Defines the ArgumentParser.

    Returns: 
      argparse.ArgumentParser
    """
    fields = dedent(
             '''
              output files:
                  db-pass
                      database of alignment records with functionality information,
                      V and J calls, and a junction region.
                  db-fail
                      database with records that fail due to no functionality information
                      (did not pass IMGT), no V call, no J call, or no junction region.

              universal output fields:
                  SEQUENCE_ID, SEQUENCE_INPUT, SEQUENCE_VDJ, SEQUENCE_IMGT,
                  FUNCTIONAL, IN_FRAME, STOP, MUTATED_INVARIANT, INDELS,
                  V_CALL, D_CALL, J_CALL,
                  V_SEQ_START, V_SEQ_LENGTH,
                  D_SEQ_START, D_SEQ_LENGTH, D_GERM_START, D_GERM_LENGTH,
                  J_SEQ_START, J_SEQ_LENGTH, J_GERM_START, J_GERM_LENGTH,
                  NP1_LENGTH, NP2_LENGTH,
                  JUNCTION_LENGTH, JUNCTION, GERMLINE_IMGT, 
                  FWR1_IMGT, FWR2_IMGT, FWR3_IMGT, FWR4_IMGT,
                  CDR1_IMGT, CDR2_IMGT, CDR3_IMGT

              imgt specific output fields:
                  V_GERM_START_IMGT, V_GERM_LENGTH_IMGT,
                  N1_LENGTH, N2_LENGTH, P3V_LENGTH, P5D_LENGTH, P3D_LENGTH, P5J_LENGTH,
                  D_FRAME, V_SCORE, V_IDENTITY, J_SCORE, J_IDENTITY,

              igblast specific output fields:
                  V_GERM_START_VDJ, V_GERM_LENGTH_VDJ,
                  V_EVALUE, V_SCORE, V_IDENTITY, V_BTOP,
                  J_EVALUE, J_SCORE, J_IDENTITY, J_BTOP.
                  CDR3_IGBLAST, CDR3_IGBLAST_AA, 
                  CDR3_IGBLAST_START, CDR3_IGBLAST_END

              ihmm specific output fields:
                  V_GERM_START_VDJ, V_GERM_LENGTH_VDJ, VDJ_SCORE
              ''')
                
    # Define ArgumentParser
    parser = ArgumentParser(description=__doc__, epilog=fields,
                            formatter_class=CommonHelpFormatter, add_help=False)
    group_help = parser.add_argument_group('help')
    group_help.add_argument('--version', action='version',
                            version='%(prog)s:' + ' %s-%s' %(__version__, __date__))
    group_help.add_argument('-h', '--help', action='help', help='show this help message and exit')
    subparsers = parser.add_subparsers(title='subcommands', dest='command',
                                       help='Aligner used', metavar='')
    # TODO:  This is a temporary fix for Python issue 9253
    subparsers.required = True

    # Parent parser
    parser_parent = getCommonArgParser(db_in=False, log=False)

    # IgBlast Aligner
    parser_igblast = subparsers.add_parser('igblast', parents=[parser_parent],
                                           formatter_class=CommonHelpFormatter, add_help=False,
                                           help='Process IgBLAST output.',
                                           description='Process IgBLAST output.')
    group_igblast = parser_igblast.add_argument_group('aligner parsing arguments')
    group_igblast.add_argument('-i', nargs='+', action='store', dest='aligner_files',
                                required=True,
                                help='''IgBLAST output files in format 7 with query sequence
                                     (IgBLAST argument \'-outfmt "7 std qseq sseq btop"\').''')
    group_igblast.add_argument('-r', nargs='+', action='store', dest='repo', required=True,
                                help='''List of folders and/or fasta files containing
                                     IMGT-gapped germline sequences corresponding to the
                                     set of germlines used in the IgBLAST alignment.''')
    group_igblast.add_argument('-s', action='store', nargs='+', dest='seq_files',
                                required=True,
                                help='''List of input FASTA files (with .fasta, .fna or .fa
                                     extension), containing sequences.''')
    group_igblast.add_argument('--partial', action='store_true', dest='partial',
                                help='''If specified, include incomplete V(D)J alignments in
                                     the pass file instead of the fail file.''')
    group_igblast.add_argument('--scores', action='store_true', dest='parse_scores',
                                help='''Specify if alignment score metrics should be
                                     included in the output. Adds the V_SCORE, V_IDENTITY,
                                     V_EVALUE, V_BTOP, J_SCORE, J_IDENTITY,
                                     J_BTOP, and J_EVALUE columns.''')
    group_igblast.add_argument('--regions', action='store_true', dest='parse_regions',
                                help='''Specify if IMGT FWR and CDRs should be
                                     included in the output. Adds the FWR1_IMGT, FWR2_IMGT,
                                     FWR3_IMGT, FWR4_IMGT, CDR1_IMGT, CDR2_IMGT, and
                                     CDR3_IMGT columns.''')
    group_igblast.add_argument('--cdr3', action='store_true',
                                dest='parse_igblast_cdr3', 
                                help='''Specify if the CDR3 sequences generated by IgBLAST 
                                     should be included in the output. Adds the columns
                                     CDR3_IGBLAST_NT and CDR3_IGBLAST_AA. Requires IgBLAST
                                     version 1.5 or greater.''')
    group_igblast.add_argument('--asis-id', action='store_true', dest='asis_id',
                                help='''Specify to prevent input sequence headers from being parsed
                                    to add new columns to database. Parsing of sequence headers requires
                                    headers to be in the pRESTO annotation format, so this should be specified
                                    when sequence headers are incompatible with the pRESTO annotation scheme.
                                    Note, unrecognized header formats will default to this behavior.''')
    group_igblast.add_argument('--asis-calls', action='store_true', dest='asis_calls',
                                help='''Specify to prevent gene calls from being parsed into standard allele names
                                     in both the IgBLAST output and reference database. Note, this requires
                                     the sequence identifiers in the reference sequence set and the IgBLAST
                                     database to be exact string matches.''')
    parser_igblast.set_defaults(func=parseIgBLAST)

    # IMGT aligner
    parser_imgt = subparsers.add_parser('imgt', parents=[parser_parent],
                                        formatter_class=CommonHelpFormatter, add_help=False,
                                        help='''Process IMGT/HighV-Quest output
                                             (does not work with V-QUEST).''',
                                        description='''Process IMGT/HighV-Quest output
                                             (does not work with V-QUEST).''')
    group_imgt = parser_imgt.add_argument_group('aligner parsing arguments')
    group_imgt.add_argument('-i', nargs='+', action='store', dest='aligner_files',
                             help='''Either zipped IMGT output files (.zip or .txz) or a
                                  folder containing unzipped IMGT output files (which must
                                  include 1_Summary, 2_IMGT-gapped, 3_Nt-sequences,
                                  and 6_Junction).''')
    group_imgt.add_argument('-s', nargs='*', action='store', dest='seq_files', required=False,
                            help='''List of FASTA files (with .fasta, .fna or .fa
                                  extension) that were submitted to IMGT/HighV-QUEST. 
                                  If unspecified, sequence identifiers truncated by IMGT/HighV-QUEST
                                  will not be corrected.''')
    group_imgt.add_argument('-r', nargs='+', action='store', dest='repo', required=False,
                            help='''List of folders and/or fasta files containing
                                 IMGT-gapped germline sequences corresponding to the
                                 set of germlines used by IMGT/HighV-QUEST. If unspecified, 
                                 the germline sequence reconstruction will not be included in 
                                 the output.''')
    group_imgt.add_argument('--asis-id', action='store_true', dest='asis_id',
                             help='''Specify to prevent input sequence headers from being parsed
                                  to add new columns to database. Parsing of sequence headers requires
                                  headers to be in the pRESTO annotation format, so this should be specified
                                  when sequence headers are incompatible with the pRESTO annotation scheme.
                                  Note, unrecognized header formats will default to this behavior.''')
    group_imgt.add_argument('--partial', action='store_true', dest='partial',
                             help='''If specified, include incomplete V(D)J alignments in
                                  the pass file instead of the fail file.''')
    group_imgt.add_argument('--scores', action='store_true', dest='parse_scores',
                             help='''Specify if alignment score metrics should be
                                  included in the output. Adds the V_SCORE, V_IDENTITY,
                                  J_SCORE and J_IDENTITY.''')
    group_imgt.add_argument('--regions', action='store_true', dest='parse_regions',
                             help='''Specify if IMGT FWRs and CDRs should be
                                  included in the output. Adds the FWR1_IMGT, FWR2_IMGT,
                                  FWR3_IMGT, FWR4_IMGT, CDR1_IMGT, CDR2_IMGT, and
                                  CDR3_IMGT columns.''')
    group_imgt.add_argument('--junction', action='store_true', dest='parse_junction',
                             help='''Specify if detailed junction fields should be
                                  included in the output. Adds the columns 
                                  N1_LENGTH, N2_LENGTH, P3V_LENGTH, P5D_LENGTH, P3D_LENGTH,
                                  P5J_LENGTH, D_FRAME.''')
    parser_imgt.set_defaults(func=parseIMGT)

    # iHMMuneAlign Aligner
    parser_ihmm = subparsers.add_parser('ihmm', parents=[parser_parent],
                                        formatter_class=CommonHelpFormatter, add_help=False,
                                        help='Process iHMMune-Align output.',
                                        description='Process iHMMune-Align output.')
    group_ihmm = parser_ihmm.add_argument_group('aligner parsing arguments')
    group_ihmm.add_argument('-i', nargs='+', action='store', dest='aligner_files',
                             required=True,
                             help='''iHMMune-Align output file.''')
    group_ihmm.add_argument('-r', nargs='+', action='store', dest='repo', required=True,
                             help='''List of folders and/or FASTA files containing
                                  IMGT-gapped germline sequences corresponding to the
                                  set of germlines used in the IgBLAST alignment.''')
    group_ihmm.add_argument('-s', action='store', nargs='+', dest='seq_files',
                             required=True,
                             help='''List of input FASTA files (with .fasta, .fna or .fa
                                  extension) containing sequences.''')
    group_ihmm.add_argument('--asis-id', action='store_true', dest='asis_id',
                             help='''Specify to prevent input sequence headers from being parsed
                                  to add new columns to database. Parsing of sequence headers requires
                                  headers to be in the pRESTO annotation format, so this should be specified
                                  when sequence headers are incompatible with the pRESTO annotation scheme.
                                  Note, unrecognized header formats will default to this behavior.''')
    group_ihmm.add_argument('--partial', action='store_true', dest='partial',
                             help='''If specified, include incomplete V(D)J alignments in
                                  the pass file instead of the fail file.''')
    group_ihmm.add_argument('--scores', action='store_true', dest='parse_scores',
                             help='''Specify if alignment score metrics should be
                                  included in the output. Adds the path score of the
                                  iHMMune-Align hidden Markov model to VDJ_SCORE.''')
    group_ihmm.add_argument('--regions', action='store_true', dest='parse_regions',
                             help='''Specify if IMGT FWRs and CDRs should be
                                  included in the output. Adds the FWR1_IMGT, FWR2_IMGT,
                                  FWR3_IMGT, FWR4_IMGT, CDR1_IMGT, CDR2_IMGT, and
                                  CDR3_IMGT columns.''')
    parser_ihmm.set_defaults(func=parseIHMM)

    return parser
    
    
if __name__ == "__main__":
    """
    Parses command line arguments and calls main
    """
    parser = getArgParser()
    checkArgs(parser)
    args = parser.parse_args()
    args_dict = parseCommonArgs(args, in_arg='aligner_files')

    # Set no ID parsing if sequence files are not provided
    if 'seq_files' in args_dict and not args_dict['seq_files']:
        args_dict['asis_id'] = True

    # Delete
    if 'aligner_files' in args_dict: del args_dict['aligner_files']
    if 'seq_files' in args_dict: del args_dict['seq_files']
    if 'out_files' in args_dict: del args_dict['out_files']
    if 'command' in args_dict: del args_dict['command']
    if 'func' in args_dict: del args_dict['func']           
    
    # Call main
    for i, f in enumerate(args.__dict__['aligner_files']):
        args_dict['aligner_file'] = f
        args_dict['seq_file'] = args.__dict__['seq_files'][i] \
                                if args.__dict__['seq_files'] else None
        args_dict['out_file'] = args.__dict__['out_files'][i] \
                                if args.__dict__['out_files'] else None
        args.func(**args_dict)
