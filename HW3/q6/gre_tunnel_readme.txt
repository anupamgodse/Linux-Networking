Creating a tunnel in gre mode between two namespaces, each connected to a VM such that VMs can have L3 connectivity

Topology is as follows:

ns3_vm (VM)
  |
  |
  |
ns3-br (bridge)                       
  |                                      ns4-vm (VM)
  |                                         |
  |                                         |
 ns3                                        |
(namespace)                                ns4-br (bridge)
  |--->(endpoint1)                          |
  |                                         | 
  |                                         |
ns_transit                                 ns4
(namespace)----------------------------(namespace)
                                      |
                                     (endpoint2)

Here we assume that ns3 namespace has defaute route via ns_transit and 
ns4 namespace has default route via ns_transit. Also default routes are VMs are configured to pass traffic to coreesponding namespaces.


The script gre_tunnel.sh creates/deletes a gre tunnel between ns3 and ns4.

The script takes following arguments in exact order as shown below.

To add/del tunnel:
./gre_tunnel <action> <tunnel_name> <ns3> <endpoint1_ip> <ns3_vm_ip> \
 <ns4> <endpoint2_ip> <ns4_vm_ip>

--action is add or del
Rest parameters are self explanatory

Example:

To add/del gre_tunnel
./gre_tunnel <action> gretun1 ns3 192.168.124.198 192.168.133.1 ns4 \
192.168.125.198 192.168.233.1
