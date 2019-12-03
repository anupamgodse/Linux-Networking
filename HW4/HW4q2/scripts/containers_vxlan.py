#This script will create two client containers in different subnets and connect them to DIFFERENT leaf containers
#It will also connect those two subnets to GRE (created in initial setup)

import docker
import sys
import os
import ipaddress
import random

cli=docker.APIClient(base_url='unix://var/run/docker.sock')

#params
#container names
c1=sys.argv[1]
c2=sys.argv[2]

l_name1="LC1"
l_name2="LC2"

l_names=[l_name1, l_name2]

c_list=[c1, c2]

b_names=[]
endpoints=[]

for i, cid in enumerate(c_list):
    nid=1 #dummy
    with open('var/nid.txt') as f:
        nid = int(f.readline())

    print(nid)

    b_name="brns"+str(nid)
    b_names.append(b_name)
    l_name=l_names[i]

    dns_ip=""
    br_ip=None
    if i==0:
        #Run DHCP server only for the first container network
        dns_ip="19.1."+str(nid)+".0/24"
        br_ip="19.1."+str(nid)+".1"
    else:
        br_ip="19.1."+str(nid-1)+".1"

    os.system("python3 scripts/create_subnet.py "+b_name+" "+l_name+" "+dns_ip)
    print("python3 scripts/create_subnet.py "+b_name+" "+l_name+" "+dns_ip)

    ip_bns=cli.inspect_container(b_name)['NetworkSettings']['Networks'][b_name+'_'+l_name]['IPAddress']
    endpoints.append(ip_bns)
    
    for spine in ['SC1', 'SC2']:
        ip_lns=cli.inspect_container(l_name)['NetworkSettings']['Networks'][l_name+'_'+spine]['IPAddress']
        os.system("ip netns exec "+spine+" ip route add "+ip_bns+" via "+ip_lns)
        print("ip netns exec "+spine+" ip route add "+ip_bns+" via "+ip_lns)

    if i==1:
        os.system("scripts/vxlan.sh add vxlan0 42 "+b_names[0]+" "+endpoints[0]+" "+b_names[0]+"_br "+b_names[1]+" "+endpoints[1]+" "+b_names[1]+"_br")
        print("scripts/vxlan.sh add vxlan0 42 "+b_names[0]+" "+endpoints[0]+" "+b_names[0]+"_br "+b_names[1]+" "+endpoints[1]+" "+b_names[1]+"_br")

    os.system("ansible-playbook -i hosts playbooks/create-container.yml -e 'c_name="+cid+"'")
    os.system("ansible-playbook -i hosts playbooks/connect-l2.yml -e 'b_name="+b_name+" c_name="+cid+" br_ip="+br_ip+"'")
    print("ansible-playbook -i hosts playbooks/create-container.yml -e 'c_name="+cid+"'")
    print("ansible-playbook -i hosts playbooks/connect-l2.yml -e 'b_name="+b_name+" c_name="+cid+" br_ip="+br_ip+"'")


    w_nid = nid+1
    os.system("echo "+str(w_nid)+" > var/nid.txt")
    print("echo "+str(w_nid)+" > var/nid.txt")

