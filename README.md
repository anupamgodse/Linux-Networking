# Linux-Networking
Linux Networking Assignments
abc
Install Ansible on Ubuntu hybervisor
$ sudo apt update
$ sudo apt install software-properties-common
$ sudo apt-add-repository --yes --update ppa:ansible/ansible
$ sudo apt install ansible


Run playbook:
sudo ansible-playbook create-vm-playbook.yml -i inventory/hosts.yml
sudo ansible-playbook load-avg-playbook.yml -i inventory/hosts.yml




ssh -Y ece792@192.168.122.71


///OVS
Create network
Attach to VM
Assign IP
Configure DHCP

Run dhclient manually

<ip address="10.10.0.1" netmask="255.255.255.0">
<dhcp>
<range start="10.10.0.2" end="10.10.0.254"/>
</dhcp>