# Linux-Networking
Linux Networking Assignments


Below are the steps followed to run the programs for Question 4 & 5

## Question 4) Ansible

Install Ansible on Ubuntu hybervisor
$ sudo apt update
$ sudo apt install software-properties-common
$ sudo apt-add-repository --yes --update ppa:ansible/ansible
$ sudo apt install ansible

Run playbook:
sudo ansible-playbook create-vm-playbook.yml -i inventory/hosts.yml
sudo ansible-playbook load-avg-playbook.yml -i inventory/hosts.yml  --extra-vars "TP=600"


## Question 5) Python lib-virt
#### 1) Host Information:    
Command: `python3 p5_python_libvirt_1.py`

#### 2) Guest Information:   
Command: `python3 p5_python_libvirt_2.py <VM_NAME>`
e.g. python3 p5_python_libvirt_2.py yjkamdarVM1

#### 2) Performance monitoring:   
Command: `python3 p5_python_libvirt_3.py <USAGE_TYPE>`
Usage types: CPU, MEM
e.g. python3 p5_python_libvirt_3.py CPU