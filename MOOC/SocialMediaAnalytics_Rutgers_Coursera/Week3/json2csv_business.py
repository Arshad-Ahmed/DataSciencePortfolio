#!/usr/bin/python
#This only works with the business dataset, to use other datasets change the lines marked in the loop below

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
root.writerow(["business_id","name","full_address","hours","open","categories","city","state","review_count","stars"])
json_no = 0 
for l in json_lines:
    root.writerow([l["business_id"], l["name"],l["full_address"],l["hours"],l["open"],l["categories"],l["city"],l["state"],l["review_count"],l["stars"]])
    json_no += 1

print('Finished {0} lines'.format(json_no)) 
OUT_FILE.close()