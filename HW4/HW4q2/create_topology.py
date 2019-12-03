import sys
import os

file_name=sys.argv[1]

with open(file_name) as f:
    for line in f:
        l = line.strip()
        values = [x.strip() for x in l.split(',')]
        CS1=values[0]
        CS2=values[1]
        action=values[2].lower()
        os.system("sudo python3 scripts/containers_"+action+".py "+CS1+" "+CS2)
        
        #print("sudo python3 scripts/containers_"+action+".py "+CS1+" "+CS2)
