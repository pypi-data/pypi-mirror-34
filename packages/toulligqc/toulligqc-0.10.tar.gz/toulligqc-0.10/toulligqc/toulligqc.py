#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#                  ToulligQC development code
#
# This code may be freely distributed and modified under the
# terms of the GNU General Public License version 3 or later
# and CeCILL. This should be distributed with the code. If you
# do not have a copy, see:
#
#      http://www.gnu.org/licenses/gpl-3.0-standalone.html
#      http://www.cecill.info/licences/Licence_CeCILL_V2-en.html
#
# Copyright for this code is held jointly by the Genomic platform
# of the Institut de Biologie de l'École Normale Supérieure and
# the individual authors.
#
# For more information on the ToulligQC project and its aims,
# visit the home page at:
#
#      https://github.com/GenomicParisCentre/toulligQC
#
#

#Production of graphs and statistics

import matplotlib
matplotlib.use('Agg')
import shutil
import sys
import csv
import re
import argparse
import os
import time
from toulligqc import fastq_extractor
from toulligqc import fast5_extractor
from toulligqc import statistics_generator
from toulligqc import albacore_1dsqr_stats_generator
from toulligqc import html_report
from toulligqc import version
from toulligqc import albacore_stats_extractor
from toulligqc import pipeline_log_extractor
from pathlib import Path
from toulligqc import toulligqc_conf


def parse_args(config_dictionary):
    '''
    Parsing the command line
    :return: config_dictionary containing the paths containing in the configuration file or specify by line arguments
    '''

    home = str(Path.home())
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--conf-file",help="Specify config file", metavar="FILE")
    parser.add_argument("-n", "--report-name", action='store', dest="report_name", help="Report name",type=str)
    parser.add_argument('-f', '--fast5-source', action='store', dest='fast5_source', help='Fast5 file source')
    parser.add_argument('-a', '--albacore-summary-source', action='store', dest='albacore_summary_source',
                        help='Albacore summary source')
    parser.add_argument('-d', '--albacore-1dsqr-summary-source', action='store', dest='albacore_1dsqr_summary_source',
                        help='Albacore 1dsq summary source',default=False)
    parser.add_argument('-p', '--albacore-pipeline-source', action='store', dest='albacore_pipeline_source',
                        help='Albacore pipeline source', default=False)
    parser.add_argument('-q', '--fastq-source', action='store', dest='fastq_source', help='Fastq file source',default=False)
    parser.add_argument('-o', '--output', action='store', dest='output', help='Output directory')
    parser.add_argument('-s', '--samplesheet-file', action='store', dest='sample_sheet_file',
                        help='Path to sample sheet file')
    parser.add_argument("-b", "--barcoding", action='store_true', dest='is_barcode', help="Barcode usage",
                        default=False)
    parser.add_argument("--quiet", action='store_true', dest='is_quiet', help="Quiet mode",
                        default=False)
    parser.add_argument("-l", "--devel-quick-launch", action='store_true', dest='is_quicklaunch', help=argparse.SUPPRESS, default=False)
    parser.add_argument('--version', action='version', version=version.__version__)

    #Parsing lone aruguments and assign each argument value to a variable
    argument_value = parser.parse_args()
    conf_file = argument_value.conf_file
    fast5_source = argument_value.fast5_source
    albacore_summary_source = argument_value.albacore_summary_source
    albacore_1dsqr_summary_source = argument_value.albacore_1dsqr_summary_source
    albacore_pipeline_source=argument_value.albacore_pipeline_source
    fastq_source = argument_value.fastq_source
    report_name = argument_value.report_name
    is_barcode = argument_value.is_barcode
    result_directory = argument_value.output
    sample_sheet_file = argument_value.sample_sheet_file
    is_quiet = argument_value.is_quiet
    is_quicklaunch = argument_value.is_quicklaunch

    config_dictionary['report_name'] = report_name

    #Checking of the presence of a configuration file
    if argument_value.conf_file:
        config_dictionary.load(conf_file)
    elif os.path.isfile(home + '/.toulligqc/config.txt'):
        config_dictionary.load(home + '/.toulligqc/config.txt')

    #Rewrite the configuration file value if argument option is present
    source_file = {
        ('fast5_source', fast5_source),
        ('albacore_summary_source', albacore_summary_source),
        ('albacore_1dsqr_summary_source', albacore_1dsqr_summary_source),
        ('albacore_pipeline_source',albacore_pipeline_source),
        ('fastq_source', fastq_source),
        ('result_directory', result_directory),
        ('sample_sheet_file', sample_sheet_file),
        ('barcoding', is_barcode),
        ('quiet', is_quiet),
        ('is_quicklaunch', is_quicklaunch)
    }

    # Put arguments values in configuration object
    for key, value in source_file:
        if value:
            config_dictionary[key] = value

    # Directory paths must ends with '/'
    for key, value in config_dictionary.items():
        if type(value) == str and os.path.isdir(value) and (not value.endswith('/')):
            config_dictionary[key] = value + '/'

    # Convert all configuration values in strings
    for key, value in config_dictionary.items():
        config_dictionary[key] = str(value)

    return config_dictionary

def check_conf(config_dictionary):
    '''
    Check the configuration
    :param config_dictionary: configuration dictionary containing the file or directory paths
    '''

    if 'fast5_source' not in config_dictionary or not config_dictionary['fast5_source']:
        sys.exit('The fast5 source argument is empty')

    if 'albacore_summary_source' not in config_dictionary or not config_dictionary['albacore_summary_source']:
         sys.exit('The albacore summary source argument is empty')

    if config_dictionary['barcoding'] == 'True':
        if not config_dictionary['sample_sheet_file']:
            sys.exit('The sample sheet source argument is empty')

    if 'result_directory' not in config_dictionary or not config_dictionary['result_directory']:
        sys.exit('The output directory argument is empty')


    # Create the root output directory if not exists
    if not os.path.isdir(config_dictionary['result_directory']):
        os.makedirs(config_dictionary['result_directory'])

    # Define the output directory
    config_dictionary['result_directory'] = config_dictionary['result_directory'] + '/' + config_dictionary['report_name'] + '/'

    if os.path.isdir(config_dictionary['result_directory']):
        shutil.rmtree(config_dictionary['result_directory'], ignore_errors=True)
        os.makedirs(config_dictionary['result_directory'])
    else:
        os.makedirs(config_dictionary['result_directory'])

def get_barcode(samplesheet):
    '''
    Get the barcode from a file given in input
    :param samplesheet: sample sheet directory
    :return: sorted list containing the barcode indicated in the sample sheet
    '''
    barcode_file = samplesheet

    set_doublon = set()

    with open(barcode_file) as csvfile:
        spamreader = csv.reader(csvfile, delimiter='\t')

        for row in spamreader:

            # Do not handle comment lines
            if row[0].startswith('#'):
                continue

            pattern = re.search(r'BC(\d{2})', row[0])

            if pattern:
                barcode = 'barcode{}'.format(pattern.group(1))
                set_doublon.add(barcode)

    return sorted(set_doublon)

def create_output_directories(config_dictionary):
    '''
    Create output directories
    :param config_dictionary: configuration dictionnary
    '''
    image_directory = config_dictionary['result_directory'] + 'images/'
    statistic_directory = config_dictionary['result_directory'] + 'statistics/'
    os.makedirs(image_directory)
    os.makedirs(statistic_directory)

def _welcome(config_dictionary):
    '''
    Print welcome message
    '''
    _show(config_dictionary, "ToulligQC version " + config_dictionary['app.version'])

def _show(config_dictionary, msg):
    '''
    Print a message on the screen
    :param config_dictionary: configuration dictionnary
    :param msg: message to print
    '''
    if 'quiet' not in config_dictionary or config_dictionary['quiet'].lower() != 'true':
        print(msg)

def _format_time(t):
    '''
    Format a time duration for humans
    :param t: time in milliseconds
    :return: a string with the duration
    '''

    return time.strftime("%H:%M:%S", time.gmtime(t))

def main():
    '''
    Main function creating graphs and statistics
    '''
    config_dictionary = toulligqc_conf.toulligqc_conf()
    parse_args(config_dictionary)
    check_conf(config_dictionary)
    create_output_directories(config_dictionary)

    if not config_dictionary:
        sys.exit("Error, dico_path is empty")

    if config_dictionary['barcoding'].lower() == 'true':
        sample_sheet_file = config_dictionary['sample_sheet_file']
        barcode_selection = get_barcode(sample_sheet_file)
        config_dictionary['barcode_selection'] = barcode_selection
        if barcode_selection == '':
            print("Sample sheet is empty")
            sys.exit(0)
    else:
        config_dictionary['barcode_selection'] = ''

    if os.path.isdir(config_dictionary['albacore_summary_source']):
        config_dictionary['albacore_summary_source'] = config_dictionary['albacore_summary_source'] + config_dictionary['report_name'] + '/sequencing_summary.txt'

    # Print welcome message
    _welcome(config_dictionary)

    #Production of the extractors object

    extractors = [fast5_extractor.fast5_extractor(config_dictionary)]

    if 'albacore_pipeline_source' in config_dictionary and config_dictionary['albacore_pipeline_source']:
        extractors.append(pipeline_log_extractor.albacore_log_extractor(config_dictionary))

    if 'fastq_source' in config_dictionary and config_dictionary['fastq_source']:
        extractors.append(fastq_extractor.fastq_extractor(config_dictionary))

    # if config_dictionary['is_quicklaunch'].lower() != 'true':
    #     extractors.append(pipeline_log_extractor.albacore_log_extractor(config_dictionary))

    if 'albacore_1dsqr_summary_source' in config_dictionary and config_dictionary['albacore_1dsqr_summary_source']:
        extractors.append(albacore_1dsqr_stats_generator.albacore_1dsqr_stats_extractor(config_dictionary))
    else:
        extractors.append(albacore_stats_extractor.albacore_stats_extractor(config_dictionary))

    #Configuration checking and initialisation of the extractors
    _show(config_dictionary, "* Initialize extractors")
    for extractor in extractors:
        extractor.check_conf()
        extractor.init()

    result_dict = {}
    graphs = []
    qc_start = time.time()

    # Initialisation if --albacore-pipeline-source not in config-dictionnry
    result_dict['albacore_version'] = "Unknown"
    result_dict['kit_version'] = "Unknown"
    result_dict['flowcell_version'] = "Unknown"
    result_dict['raw_fast5'] = -1
    result_dict['fast5_failed_to_load_key'] = -1
    result_dict['fast5_failed_count'] = -1
    result_dict['fast5_processed'] = -1
    result_dict['raw_fast5_no_processed'] = -1
    result_dict['basecalled_error_count'] = -1
    result_dict['parsing_fastq'] = False

    #Information extraction about statistics and generation of the graphs
    for extractor in extractors:
        _show(config_dictionary, "* Start {0} extractor".format(extractor.get_name()))

        extractor_start = time.time()
        extractor.extract(result_dict)
        graphs.extend(extractor.graph_generation(result_dict))
        extractor.clean()
        extractor_end = time.time()

        _show(config_dictionary, "* End of {0} extractor (done in {1})".format(extractor.get_name(), _format_time(extractor_end - extractor_start)))

    #HTML report and statistics file generation
    _show(config_dictionary, "* Write HTML report")
    html_report.html_report(config_dictionary, result_dict, graphs)

    if config_dictionary['is_quicklaunch'].lower() != 'true':
        _show(config_dictionary, "* Write statistics files")
        statistics_generator.statistics_generator(config_dictionary, result_dict)
        statistics_generator.save_result_file(config_dictionary, result_dict)

    qc_end = time.time()
    _show(config_dictionary, "* End of the QC extractor (done in {1})".format(extractor.get_name(), _format_time(qc_end - qc_start)))

if __name__ == "__main__":
    main()
