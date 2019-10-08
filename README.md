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
sudo ansible-playbook load-avg-playbook.yml -i inventory/hosts.yml  --extra-vars "TP=600"
