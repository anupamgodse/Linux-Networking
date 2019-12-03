#This script will create two client containers in different subnets and connect them to DIFFERENT leaf containers
#It will also connect those two subnets to GRE (created in initial setup)

import docker
import sys
import os
import ipaddress
import random

#params
#container names
c1=sys.argv[1]
c2=sys.argv[2]

l_name1="LC1"
l_name2="LC2"

l_names=[l_name1, l_name2]

c_list=[c1, c2]

for i, cid in enumerate(c_list):
    nid=1 #dummy
    with open('var/nid.txt') as f:
        nid = int(f.readline())

    #print(nid)

    b_name="brns"+str(nid)
    l_name=l_names[i]
    dns_ip="19.1."+str(nid)+".0/24"
    br_ip="19.1."+str(nid)+".1"

    os.system("python3 scripts/create_subnet.py "+b_name+" "+l_name+" "+dns_ip)
    #print("python3 scripts/create_subnet.py "+b_name+" "+l_name+" "+dns_ip)


    os.system("ansible-playbook -i hosts playbooks/create-container.yml -e 'c_name="+cid+"'")
    os.system("ansible-playbook -i hosts playbooks/connect-l2.yml -e 'b_name="+b_name+" c_name="+cid+" br_ip="+br_ip+"'")
    #print("ansible-playbook -i hosts playbooks/create-container.yml -e 'c_name="+cid+"'")
    #print("ansible-playbook -i hosts playbooks/connect-l2.yml -e 'b_name="+b_name+" c_name="+cid+" br_ip="+br_ip+"'")


    #Add cs1 route to leaf container 2 
    if(cid == c1):
        os.system("ip netns exec "+l_name2+" ip route add "+dns_ip+" dev gretun1")
    else:
        os.system("ip netns exec "+l_name1+" ip route add "+dns_ip+" dev gretun1")
        
    w_nid = nid+1

    os.system("echo "+str(w_nid)+" > var/nid.txt")
    #print("echo "+str(w_nid)+" > var/nid.txt")
