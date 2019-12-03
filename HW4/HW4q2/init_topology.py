import os
import sys
import docker

cli=docker.APIClient(base_url='unix://var/run/docker.sock')

lc_los = ["39.0.0.1", "40.0.0.1"]

spines=sys.argv[1].split(',')
leafs=sys.argv[2].split(',')

for node in spines+leafs:
    cmd="ansible-playbook -i hosts playbooks/create-container.yml -e 'c_name="+node+"'"
    os.system(cmd)

for i, leaf in enumerate(leafs):
    os.system("ip netns exec "+leaf+" ip addr add "+lc_los[i]+"/32 dev lo")
    #print("ip netns exec "+leaf+" ip addr add "+lc_los[i]+" dev lo")
    for spine in spines:
        cmd="ansible-playbook -i hosts playbooks/connect-l3.yml -e 'c_name_1="+leaf+" c_name_2="+spine+"'"
        os.system(cmd)
        ip=cli.inspect_container(leaf)['NetworkSettings']['Networks'][leaf+'_'+spine]['IPAddress']
        os.system("ip netns exec "+spine+" ip route add "+lc_los[i]+"/32 via "+ip)
        #print("ip netns exec "+spine+" ip route add "+lc_los[i]+" via "+ip)

    cmd="python3 scripts/leaf_route.py "+leaf+" "+sys.argv[1]
    os.system(cmd)


#create GRE tunnel between LC1 and LC2
os.system("scripts/gre_tunnel_hw4.sh add gretun1 "+leafs[0]+" "+lc_los[0]+" "+leafs[1]+" "+lc_los[1])
#print("scripts/gre_tunnel_hw4.sh add gretun1 "+leafs[0]+" "+lc_los[0]+" "+leafs[1]+" "+lc_los[1])

os.system("mkdir -p var/")
os.system("echo 1 > var/nid.txt")
