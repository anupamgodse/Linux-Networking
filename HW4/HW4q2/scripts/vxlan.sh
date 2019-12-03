#single pt vxlan

#Assumed that the infrastructure shown in vxlan_readme.sh is already present

#add or delete tunnel
action=$1

#name of tunnel
name=$2

#id
id=$3

#Name of namespaces as endpoints and corresponding ip addresses
#Refer readme for topology
ns1=$4
ns1_ip=$5
ns1_br=$6

ns2=$7
ns2_ip=$8
ns2_br=$9


if [ $action = "add" ]; then

	#at ns1
	sudo ip netns exec $ns1 ip link add $name type vxlan id $id remote $ns2_ip local $ns1_ip dstport 4789
	sudo ip netns exec $ns1 ip link set $name up
	sudo ip netns exec $ns1 brctl addif $ns1_br $name

	#at ns2
	sudo ip netns exec $ns2 ip link add $name type vxlan id $id remote $ns1_ip local $ns2_ip dstport 4789
	sudo ip netns exec $ns2 ip link set $name up
	sudo ip netns exec $ns2 brctl addif $ns2_br $name
elif [ $action = "del" ]; then
	sudo ip netns exec $ns1 ip link del $name type vxlan id $id remote $ns2_ip local $ns1_ip dstport 4789
	sudo ip netns exec $ns2 ip link del $name type vxlan id $id remote $ns1_ip local $ns2_ip dstport 4789
fi
