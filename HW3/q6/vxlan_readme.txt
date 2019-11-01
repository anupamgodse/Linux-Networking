#Assumed setup

bridge-----vxlan_dev-----endpoint1 (namespace1)
                            |
                            |
			    |
                         ns_transit (namespace)
                            |
                            |
			    |
bridge-----vxlan_dev-----endpoint2 (namespace2)

Note that vxlan device and bridge are contained within coreesponding namespaces.

It is assumed that the default routes are configured at VMs connected to bridges and at namespaces.

Also the bridge is already existing bridge at both namespaces.

#add/del a vxlan tunnel between two endpoints

./vxlan.sh <action> <vxlan_dev_name> <vxlan_id> <namespace_1> <endpoint_1_ip> <namespace_1_bridge> <namespace_2> <endpoint_2_ip> <namespace_2_bridge>

--action is add/del
Rest params are selfexplanatory
