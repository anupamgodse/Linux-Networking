import docker
import sys
import os

cli=docker.APIClient(base_url='unix://var/run/docker.sock')

l_name=sys.argv[1]
spines=sys.argv[2].split(',')

ns_cmd='ip netns exec '+l_name
route_str=' ip route add default scope global '

for spine in spines:
    ip=cli.inspect_container(spine)['NetworkSettings']['Networks'][l_name+'_'+spine]['IPAddress']
    route_str+='nexthop via '+ip+' weight 1 '

os.system(ns_cmd+' ip route del default')
os.system(ns_cmd+route_str)

