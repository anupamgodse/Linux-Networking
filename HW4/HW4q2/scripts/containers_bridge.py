"""This script will create two client containers and connect them to same bridge
which will be connected to a random leaf container (LC1 or LC2) if arg3 is not given
otherwise will be connected to LC corresponding to arg3"""

import docker
import sys
import os
import ipaddress
import random

leaf_selected=False

#params
#container names
c1=sys.argv[1]
c2=sys.argv[2]
#which leaf number to connect (optional)

print(sys.argv)
if(len(sys.argv) > 3):
    l_id = sys.argv[3]
else:
    l_id = str(random.randint(1,2))

nid=1
with open('var/nid.txt') as f:
    nid = int(f.readline())

#print(nid)

b_name="brns"+str(nid)
l_name='LC'+l_id
dns_ip="19.1."+str(nid)+".0/24"
br_ip="19.1."+str(nid)+".1"

os.system("python3 scripts/create_subnet.py "+b_name+" "+l_name+" "+dns_ip)
#print("python3 scripts/create_subnet.py "+b_name+" "+l_name+" "+dns_ip)

c_list=[c1, c2]

for cid in c_list:
    os.system("ansible-playbook -i hosts playbooks/create-container.yml -e 'c_name="+cid+"'")
    os.system("ansible-playbook -i hosts playbooks/connect-l2.yml -e 'b_name="+b_name+" c_name="+cid+" br_ip="+br_ip+"'")
    #print("ansible-playbook -i hosts playbooks/create-container.yml -e 'c_name="+cid+"'")
    #print("ansible-playbook -i hosts playbooks/connect-l2.yml -e 'b_name="+b_name+" c_name="+cid+" br_ip="+br_ip+"'")
    
w_nid = nid+1

os.system("echo "+str(w_nid)+" > var/nid.txt")
#print("echo "+str(w_nid)+" > var/nid.txt")
