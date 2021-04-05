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

spreadsheet_data = [[], [], []]

spreadsheet_data[0].append("timestamp")
spreadsheet_data[1].append("")
spreadsheet_data[2].append("")

spreadsheet_data[0].append("user_id")
spreadsheet_data[1].append("")
spreadsheet_data[2].append("")

spreadsheet_data[0].append("demogr_edu")
spreadsheet_data[1].append("")
spreadsheet_data[2].append("")

spreadsheet_data[0].append("demogr_exp")
spreadsheet_data[1].append("")
spreadsheet_data[2].append("")

spreadsheet_data[0].append("demogr_role")
spreadsheet_data[1].append("")
spreadsheet_data[2].append("")

spreadsheet_data[0].append("demogr_role_exp")
spreadsheet_data[1].append("")
spreadsheet_data[2].append("")

spreadsheet_data[0].append("demogr_role_desc")
spreadsheet_data[1].append("")
spreadsheet_data[2].append("")

for index_p, key in enumerate(csv_keys):
    for index_q, value in enumerate(csv_data[key]):
        if value == "X":
            continue
        
        qid_f = "p" + str(index_p + 1) + "_" + "q" + str(index_q + 1) + "_f"
        qid_i = "p" + str(index_p + 1) + "_" + "q" + str(index_q + 1) + "_i"

        spreadsheet_data[0].append(qid_f)
        spreadsheet_data[0].append(qid_i)

        spreadsheet_data[1].append(value)
        spreadsheet_data[1].append("")

    for index_c in range(0, 10):
        qid_s = "p" + str(index_p + 1) + "_" + "c" + str(index_c + 1) + "_s"
        qid_f = "p" + str(index_p + 1) + "_" + "c" + str(index_c + 1) + "_f"
        qid_i = "p" + str(index_p + 1) + "_" + "c" + str(index_c + 1) + "_i"

        spreadsheet_data[0].append(qid_s)
        spreadsheet_data[0].append(qid_f)
        spreadsheet_data[0].append(qid_i)

        spreadsheet_data[1].append("custom question " + str(index_c + 1))
        spreadsheet_data[1].append("")
        spreadsheet_data[1].append("")

    spreadsheet_data[2].append(key)
    while len(spreadsheet_data[2]) != len(spreadsheet_data[0]):
        spreadsheet_data[2].append("")

with open(os.path.join(cwd, "spreadsheet.csv"), "w", newline = "") as file_object:
    writer = csv.writer(file_object)
    writer.writerows(spreadsheet_data)
