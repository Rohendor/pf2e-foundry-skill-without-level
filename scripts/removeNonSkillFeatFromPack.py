import csv
import os
import json
from pathlib import Path

path = "/home/rohendor/FVTT/FoundryVTT/ProjectSandro/pf2e-rohendor/packs/data/feats.db/"
filepath = path
count = 0

for (root, dirs, file) in os.walk(path):
        for f in file:
                found = False
                js = open(filepath + f)
                data = json.load(js)
                if (data['system']['featType']['value']!="skill"):
                        found = True
                js.close
                if (found):
                        os.remove(Path(filepath + f))
                        found = False

print (str(count) +" files moved")
