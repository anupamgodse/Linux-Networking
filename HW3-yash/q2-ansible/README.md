Generating a sample VM:
virt-builder centos-7.4  --install iperf3,wireshark --format qcow2 -o /var/lib/libvirt/images/sampleVM.img

Config files:
nw_config :: Consists of ovs-infra and network configurations
vm_config :: Consists of info for the VM and its mapped interfaces

Create:
sudo ansible-playbook create-infra-playbook.yml -i inventory/hosts.yml

Delete:
sudo ansible-playbook delete-infra-playbook.yml -i inventory/hosts.yml

Bonus:
sudo ansible-playbook create-vms.yml -i inventory/hosts.yml --extra-vars @vars/vm_config_test.yml

Run above command to create VMs basis of user provided input. Provide a files path containing the VM to be created in a file of below format.
<!-- 
VMs: 
  - name: VM1-yk
    networks: [Internet-yk,L2-yk]
  - name: VM2-yk
    networks: [Internet-yk,L2-yk] 
-->