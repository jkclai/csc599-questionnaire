#!/usr/bin/python3

import os
import re
import csv
import sys

import pandas as pd

if len(sys.argv) == 1:
    cwd = os.getcwd()
else:
    cwd = sys.argv[1]

file = ""

for files in os.listdir(cwd):
    if files == "data.csv":
        file = os.path.join(cwd, files)

if file == "":
    exit()

with open(file, "r") as file_object:
    file_rows = [row.strip().split(",") for row in file_object]

csv_data = {x[0]:list(x[1:]) for x in zip(*file_rows)}
csv_keys = list(csv_data.keys())

for index_p, key in enumerate(csv_keys):
    html = ""

    html += """<!DOCTYPE html>
<html>
"""

    html += """<head>
    <meta content="text/html;charset=utf-8" http-equiv="Content-Type">
    <meta content="utf-8" http-equiv="encoding">
    <link rel="stylesheet" href="./assets/styles/style.css">
</head>
"""

    html += """<body>
    <div class="form-wrapper">
        <h1 class="form-header">""" + key + """</h1>
        <h2 class="form-header">Page """ + str(index_p + 1) + """ of 4</h2>"""

    html += """
        <form name="submit-to-google-sheet">
            <table class="likert-block">
                <colgroup>
                    <col class="likert-table-column-statement" span="1">
                    <col class="likert-table-column-question" span="1">
                    <col class="likert-table-column-question" span="1">
                </colgroup>
                <tr class="likert-tablerow">
                    <th class="likert-tableheader">
                    </th>
                    <th class="likert-tableheader">
                        <label>How often do I ask this question?</label>
                        <div>
                            <label>never</label>
                            <label>rarely</br>(~1/month)</label>
                            <label>sometimes</br>(~1/week)</label>
                            <label>often</br>(~1/day)</label>
                            <label>frequently</br>(>1/day)</label>
                        </div>
                    </th>
                    <th class="likert-tableheader">
                        <label>How important is it to answer this question?</label>
                        <div>
                            <label>not important</label>
                            <label>low importance</label>
                            <label>neutral</label>
                            <label>important</label>
                            <label>very important</label>
                        </div>
                    </th>
                </tr>"""

    for index_q, value in enumerate(csv_data[key]):
        if value == "X":
            continue
        
        qid_f = "p" + str(index_p + 1) + "_" + "q" + str(index_q + 1) + "_f"
        qid_i = "p" + str(index_p + 1) + "_" + "q" + str(index_q + 1) + "_i"
        html_block = ""

        html_block += """
                <tr class="likert-tablerow">
                    <td class="likert-tabledata">
                        <label class="likert-data-statement">""" + value + """</label>"""

        html_block += """
                    </td>
                    <td class="likert-tabledata">
                        <div class="likert-data-question">
                            """

        for i in range(1, 6):
            html_block += """<div><input type="radio" name='""" + qid_f + "' value='" + str(i) + "' required></div>"
        
        html_block += """
                        </div>
                    </td>
                    <td class="likert-tabledata">
                        <div class="likert-data-question">
                            """

        for i in range(1, 6):
            html_block += """<div><input type="radio" name='""" + qid_i + "' value='" + str(i) + "' required></div>"

        html_block += """
                        </div>
                    </td>
                </tr>"""

        html += html_block
    
    html += """
                <tr class="likert-tablerow">
                    <td class="likert-tabledata">
                        <div class="likert-data-statement">
                            <label>Other:</label>
                            <textarea id="p""" + str(index_p + 1) + """_c1_s" name="p""" + str(index_p + 1) + """_c1_s" onclick="addCustomBlock(this.id)" placeholder="What are some questions that we missed?"></textarea>
                        </div>
                    </td>
                    <td class="likert-tabledata">
                        <div class="likert-data-question">
                            <div><input type="radio" name='p""" + str(index_p + 1) + """_c1_f' value='1'></div><div><input type="radio" name='p""" + str(index_p + 1) + """_c1_f' value='2'></div><div><input type="radio" name='p""" + str(index_p + 1) + """_c1_f' value='3'></div><div><input type="radio" name='p""" + str(index_p + 1) + """_c1_f' value='4'></div><div><input type="radio" name='p""" + str(index_p + 1) + """_c1_f' value='5'></div>
                        </div>
                    </td>
                    <td class="likert-tabledata">
                        <div class="likert-data-question">
                            <div><input type="radio" name='p""" + str(index_p + 1) + """_c1_i' value='1'></div><div><input type="radio" name='p""" + str(index_p + 1) + """_c1_i' value='2'></div><div><input type="radio" name='p""" + str(index_p + 1) + """_c1_i' value='3'></div><div><input type="radio" name='p""" + str(index_p + 1) + """_c1_i' value='4'></div><div><input type="radio" name='p""" + str(index_p + 1) + """_c1_i' value='5'></div>
                        </div>
                    </td>
                </tr>
            </table>
            <div class="form-options">
                <input type="hidden" id="user_id" name="user_id" required>
                <button type="submit" id="submit-button">Next</button>
            </div>
        </form>
    </div>
    """

    html += """
    <script src="./assets/scripts/constants.js"></script>
    """

    html += """
    <script>
        if(localStorage.getItem("user_id") == null) {
            localStorage.setItem("user_id", btoa(Math.random()));
        }
        document.getElementById("user_id").value = localStorage.getItem("user_id");
    </script>
    """

    html += """
    <script>
        function addCustomBlock(id) {
            var idArray = id.split("_");
            var p = parseInt(idArray[0].substring(1));
            var c = parseInt(idArray[1].substring(1));

            var idNew_s = "p" + p.toString() + "_c" + (c+1).toString() + "_s";
            var idNew_f = "p" + p.toString() + "_c" + (c+1).toString() + "_f";
            var idNew_i = "p" + p.toString() + "_c" + (c+1).toString() + "_i";

            if(document.getElementById(idNew_s) == null && c < 10) {
                var block = document.getElementsByClassName("likert-block")[0];
                
                var row = document.createElement("tr");
                row.className = "likert-tablerow";

                row.innerHTML = `
                    <td class="likert-tabledata">
                        <div class="likert-data-statement">
                            <label>Other:</label>
                            <textarea id="` + idNew_s + `" name="` + idNew_s + `" onclick="addCustomBlock(this.id)" placeholder="What are some questions that we missed?"></textarea>
                        </div>
                    </td>
                    <td class="likert-tabledata">
                        <div class="likert-data-question">
                            <div><input type="radio" name='` + idNew_f + `' value='1'></div><div><input type="radio" name='` + idNew_f + `' value='2'></div><div><input type="radio" name='` + idNew_f + `' value='3'></div><div><input type="radio" name='` + idNew_f + `' value='4'></div><div><input type="radio" name='` + idNew_f + `' value='5'></div>
                        </div>
                    </td>
                    <td class="likert-tabledata">
                        <div class="likert-data-question">
                            <div><input type="radio" name='` + idNew_i + `' value='1'></div><div><input type="radio" name='` + idNew_i + `' value='2'></div><div><input type="radio" name='` + idNew_i + `' value='3'></div><div><input type="radio" name='` + idNew_i + `' value='4'></div><div><input type="radio" name='` + idNew_i + `' value='5'></div>
                        </div>
                    </td>
                `; 

                block.appendChild(row);
            }
        }
    </script>
    """

    html += """
    <script>
        const form = document.forms["submit-to-google-sheet"];

        form.addEventListener("submit", e => {
            e.preventDefault();

            document.getElementById("submit-button").disabled = true;

            if(form.checkValidity()) {
                fetch("https://script.google.com/macros/s/" + SCRIPT_ID + "/exec?callback=?", {method: "POST", mode:"no-cors", body: new FormData(form)})
                    .then(response => {
                        console.log("Success!", response);
                        window.location.href = "./page""" + str(index_p + 2) + """.html";
                    })
                    .catch(error => {
                        console.error("Error!", error.message);
                        document.getElementById("submit-button").disabled = false;
                    });
            }
        })
    </script>
</body>
</html>"""

    with open(os.path.join(cwd, "page" + str(index_p + 1) + ".html"), "w", newline = "") as file_object:
        file_object.write(html)
