#Sample CSV file
CS1Q, CS2Q, Bridge
CS1X, CS2X, VXLAN
CSX, CSY, L3
CSA, CSB, GRE

To parse a csv file and create corresponding topology.
Assumed that init_topologa.py is done before this.

How to Run?
>> sudo python3 create_topology.py <path_to_csv_file>

Assumptions:
CS1Q, CS2Q, Bridge: 
Will create two containers and connect them to same bridge which will be connected to any one of the leaf containers.

CS1X, CS2X, VXLAN
Will create two containers in same subnet accross different leaf containers.

CSX, CSY, L3
Will create two containers in different subnets and connect them to any one SAME spine.

CSA, CSB, GRE
Will create two containers in different subnets and connect them to DIFFERENT leafs.
This will also add appropirate routes to leaf containers to send traffic to gre tunnel.
