Generating a sample VM:
sudo virt-builder centos-7.4  --install epel-release,iperf3,wireshark,qemu-guest-agent --format qcow2 -o /var/lib/libvirt/images/sampleBuild.img

Config files:
nw_config :: Consists of ovs-infra and network configurations
vm_config :: Consists of info for the VM and its mapped interfaces

Create:
sudo ansible-playbook create-infra-playbook.yml -i inventory/hosts.yml

Delete:
sudo ansible-playbook delete-infra-playbook.yml -i inventory/hosts.yml

Bonus:
sudo ansible-playbook create-vms.yml -i inventory/hosts.yml --extra-vars @vars/vm_config_test.yml

sudo ansible-playbook build-vms.yml -i inventory/hosts.yml --extra-vars @vars/vm_config_test.yml

Run above command to create VMs basis of user provided input. Provide a files path containing the VM to be created in a file of below format.
<!-- 
VMs: 
  - name: VM1-yk
    networks: [Internet-yk,L2-yk]
  - name: VM2-yk
    networks: [Internet-yk,L2-yk] 
-->


Uid7jQKtBAU89C4n