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

#HTML report generation
import re
import base64
import dateutil.parser
import time

def html_report(config_dictionary, result_dict, graphs):

    '''
    Creation of a html report
    :param config_dictionary: dictionary containing file or directory paths
    :param result_dict: result dictionary containing all statistics
    '''

    result_directory = config_dictionary['result_directory']
    report_name = config_dictionary['report_name']

    #from sequence summary file
    run_time = result_dict["run_time"]
    report_date= time.strftime("%x %X %Z")

    #from Fast5 file
    run_date = result_dict['exp_start_time']
    date = dateutil.parser.parse(run_date)
    run_date = date.strftime("%x %X %Z")
    flow_cell_id = result_dict['flow_cell_id']

    read_count = result_dict["fastQ_entries"]
    run_yield = round(result_dict["Yield"],2)

    #from pipeline log file
    flowcell_version = result_dict['flowcell_version']
    kit_version = result_dict['kit_version']
    run_id = result_dict['sample_id']
    minknow_version = result_dict['minknow_version']
    albacore_version = result_dict['albacore_version']


    f = open(result_directory + 'report.html', 'w')

    # Define the header of the page
    header = """<!doctype html>
<html>
  <head>
    <title>Rapport run MinION</title>
    <meta charset='UTF-8'>
    <style type="text/css">

  @media screen {

    div.summary {
      width: 16em;
      position:fixed;
      top: 4.5em;
      margin:1em 0 0 1em;
    }

    div.main {
      display:block;
      position:absolute;
      overflow:auto;
      height:auto;
      width:auto;
      top:4.5em;
      bottom:2.3em;
      left:18em;
      right:0;
      border-left: 1px solid #CCC;
      padding:0 0 0 1em;
      background-color: white;
      z-index:1;
    }

    div.header {
      background-color: #EEE;
      border:0;
      margin:0;
      padding: 0.5em;
      font-size: 200%;
      font-weight: bold;
      position:fixed;
      width:100%;
      top:0;
      left:0;
      z-index:2;
    }

    div.footer {
      background-color: #EEE;
      border:0;
      margin:0;
      padding:0.5em;
      height: 1.3em;
      overflow:hidden;
      font-size: 100%;
      font-weight: bold;
      position:fixed;
      bottom:0;
      width:100%;
      z-index:2;
    }

    img.indented {
      margin-left: 3em;
    }
  }

  @media print {

    img {
      max-width:80% !important;
      page-break-inside: avoid;
    }

    h2, h3 {
      page-break-after: avoid;
    }

    div.header {
      background-color: #FFF;
    }

  }

  body {
    font-family: sans-serif;
    color: #000;
    background-color: #FFF;
    border: 0;
    margin: 0;
    padding: 0;
  }

  div.header {
    border:0;
    margin:0;
    padding: 0.5em;
    font-size: 200%;
    font-weight: bold;
    width:100%;
  }

  #header_title {
    display:inline-block;
    float:left;
    clear:left;
  }

  #header_filename {
    display:inline-block;
    float:right;
    clear:right;
    font-size: 50%;
    margin-right:2em;
    text-align: right;
  }

  div.header h3 {
    font-size: 50%;
    margin-bottom: 0;
  }

  div.summary ul {
    padding-left:0;
    list-style-type:none;
  }

  div.summary ul li img {
    margin-bottom:-0.5em;
    margin-top:0.5em;
  }

  div.main {
    background-color: white;
  }

  div.module {
    padding-bottom:1.5em;
    padding-top:1.5em;
  }
  
  .box {
    float:left;
    min-width: 1150px;
    height: 450px;
    margin: 0em;
    padding-bottom:1.5em;
    padding-top:1.8em;
    top: 0 auto;
    bottom: 0 auto;
  }
  
    .box-left {
    float:left;
    min-width: 430px;
    height: 460px;
    margin: 0em;
    padding-bottom:1.5em;
    padding-top:1.5em;
    top: 0.3px;
    bottom: 0 auto;
  }
  
  .after-box {
    clear: left;
  }

  div.footer {
    background-color: #EEE;
    border:0;
    margin:0;
    padding: 0.5em;
    font-size: 100%;
    font-weight: bold;
    width:100%;
  }


  a {
    color: #000080;
  }

  a:hover {
    color: #800000;
  }

  h2 {
    color: #244C89;
    padding-bottom: 0;
    margin-bottom: 0;
    clear:left;
  }

  table {
    margin-left: 3em;
    text-align: center;
    border-collapse:collapse;
  }

  th {
    text-align: center;
    background-color: #244C89;
    color: #FFF;
    padding: 0.4em;
  }

  td {
    font-family: monospace;
    text-align: right;
    background-color: #EFEFEF;
    color: #000;
    padding: 0.4em;
  }

  img {
    padding-top: 0;
    margin-top: 0;
    border-top: 0;
  }
  
  p {
    padding-top: 0;
    margin-top: 0;
  }

    </style>
  </head>
  <body>
"""

    # Define the footer of the page
    footer = """
    <div class="footer"> Produced by <a href="{0}">{1}</a> (version {2})</div>
  </body>

</html>
""".format(config_dictionary['app.url'], config_dictionary['app.name'], config_dictionary['app.version'])

    # Compose the Banner of the page
    banner = """
    <div class="header">
      <div id="header_title">ToulligQC report for {0} <br/></div>
      <div id="header_filename">
        Run id: {0} <br>
        Repport name: {1} <br>
        Run date: {2} <br>
        Report date : {3} <br>
      </div>
    </div>
""".format(run_id, report_name, run_date, report_date)

    # Compose the summary section of the page
    summary = """
    <div class='summary'>
      <h2>Summary</h2>
      <ol>
"""
    for i, t in enumerate(graphs):
      summary += "        <li><a href=\"#M" + str(i) + "\">" + t[0]  + "</a></li>\n"
    summary += """      </ol>
    </div>
"""

    # Compose the main of the page
    main_report = """
    <div class = 'main'>
      <div class=\"module\">
        <h2 id=M{0}>Basic Statistics</h2>
        <table class=\" dataframe \" border="1">
          <thead>
            <th>Measure</th>
            <th>Value</th>
          </thead>
          <tbody>
          <tr>
            <th>Run id</th>
            <td> {0} </td>
          </tr>
          <tr>
            <th>Report name </th>
            <td> {1} </td>
          </tr>
          <tr>
            <th>Run date</th>
            <td> {2} </td>
          </tr>
          <tr>
            <th>Run time (h) </th>
            <td> {3} </td>
          </tr>
          <tr>
            <th>Flowcell id </th>
            <td> {4} </td>
          </tr>
          <tr>
            <th>Flowcell version</th>
            <td> {5} </td>
          </tr>
          <tr>
            <th>Kit</th>
            <td> {6} </td>
          </tr>
          <tr>
            <th>MinKNOW version </th>
            <td> {7} </td>
          </tr>
          <tr>
            <th>Albacore version</th>
            <td> {8} </td>
          </tr>
          <tr>
            <th>ToulligQC version</th>
            <td> {9} </td>
          </tr>
          <tr>
            <th>Yield (Gbp)</th>
            <td> {10} </td>
          </tr>
          <tr>
            <th>Read count</th>
            <td> {11} </td>
          </tr>
          </tbody>
        </table>   
      </div>
""".format(run_id,report_name, run_date, run_time, flow_cell_id,flowcell_version,kit_version,minknow_version,albacore_version,config_dictionary['app.version'],run_yield,read_count)

    for i, t in enumerate(graphs):
        main_report += "      <div class=\"module\"><h2 id=M{0}> {1} <img src=\"http://mikecavaliere.com/wp-content/uploads/2015/05/Question-300x300.png\" alt=\"Smiley face\" width=\"20\" height=\"25\" title=\"{4}\"> </h2></div>".format(i, t[0], _embedded_image(t[1]), t[2],t[3])
        if(t[2]==None):
            main_report += "      <div class=\"module\"><p><img src=\"{2}\" alt=\"{1} image\"></p></div>\n".format(i, t[0], _embedded_image(t[1]))
        else:
            main_report += "      <div class=\"box\"><img src=\"{2}\"></div>\n".format(i, t[0], _embedded_image(t[1]), t[2])
            main_report += "      <div class=\"box-left\"><p>{3}</p></div>\n".format(i, t[0], _embedded_image(t[1]), t[2])
            main_report += "      <div class=\"after-box\"><p></p></div>\n"
    main_report += "    </div>\n"

    # Add all the element of the page
    report = header + banner + summary + main_report + footer

    # Write the HTML page
    f.write(report)
    f.close()


def _embedded_image(image_path):
    '''
    Embedded an image
    :param image_path: path of the image
    :return: a string with the image in base64
    '''

    with open(image_path, "rb") as image_file:
        result = "data:image/png;base64," + base64.b64encode(image_file.read()).decode('ascii')

    return result

