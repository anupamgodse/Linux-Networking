import docker
import sys
import os
import ipaddress


subnet_defined=False
cli=docker.APIClient(base_url='unix://var/run/docker.sock')

b_name=sys.argv[1]
l_name=sys.argv[2]
if(len(sys.argv) > 3):
    subnet=sys.argv[3].split('/')
    ip=str(ipaddress.ip_address(subnet[0])+1)+'/'+subnet[1]
    ip_range=str(ipaddress.ip_address(subnet[0])+2)+','+str(ipaddress.ip_address(subnet[0])+254)
    subnet_defined=True

os.system("sudo ansible-playbook -i hosts playbooks/create-container.yml -e 'c_name="+b_name+"'")

if subnet_defined:
    os.system("sudo ansible-playbook -i hosts playbooks/create-bridge.yml -e 'b_name="+b_name+" ip="+ip+" range="+ip_range+"'")
else:
    os.system("sudo ansible-playbook -i hosts playbooks/create-bridge.yml -e 'b_name="+b_name+"'")

os.system("sudo ansible-playbook -i hosts playbooks/connect-l3.yml -e 'c_name_1="+b_name+" c_name_2="+l_name+"'")

ns_cmd='ip netns exec '

if subnet_defined:
    b_ip=cli.inspect_container(b_name)['NetworkSettings']['Networks'][b_name+'_'+l_name]['IPAddress']
    os.system(ns_cmd+l_name+" ip route add "+sys.argv[3]+" via "+b_ip)

l_ip=cli.inspect_container(l_name)['NetworkSettings']['Networks'][b_name+'_'+l_name]['IPAddress']
os.system(ns_cmd+b_name+" ip route del default")
os.system(ns_cmd+b_name+" ip route add default via "+l_ip)
