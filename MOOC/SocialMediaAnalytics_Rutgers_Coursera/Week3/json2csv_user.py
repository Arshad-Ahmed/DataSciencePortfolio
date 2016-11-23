#!/usr/bin/python
#This only works with the user dataset, to use other datasets change the lines marked in the loop below

import sys
import json
import csv

ifilename = sys.argv[1]
try:
    ofilename = sys.argv[2]
except:
    ofilename = ifilename + ".csv"

# LOAD DATA
json_lines = [json.loads( l.strip() ) for l in open(ifilename).readlines() ]
OUT_FILE = open(ofilename, "w")
root = csv.writer(OUT_FILE)
root.writerow(["user_id","name","review_count","average_stars","cool_votes","funny_votes","useful_votes","friends","elite","yelping_since","fans"])
json_no = 0 
for l in json_lines:
    root.writerow([l["user_id"], l["name"],l["review_count"],l["average_stars"],l["votes"]["cool"],l["votes"]["funny"],l["votes"]["useful"],l["friends"],l["elite"],l["yelping_since"],l["fans"]])
    json_no += 1

print('Finished {0} lines'.format(json_no)) 
OUT_FILE.close()