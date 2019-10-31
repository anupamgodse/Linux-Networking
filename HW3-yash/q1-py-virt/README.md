Notes:Ensure Guest-agent is installed in all VMs, if not then install using
yum install qemu-guest-agent

Verify from Hypervisor:
virsh qemu-agent-command VM1-yk '{"execute":"guest-network-get-interfaces"}'

Another approach would be to fetch the IP from the dnsmasq leases file on the hypervisor (/var/lib/misc/dnsmasq.leases),
but my approach would fetch even the static IPs set in the guest VM.

Steps to run:

Local hypervisor:
python resolve_conflict.py

For Remote hypervisors:
Make sure to have the ssh private key in your system that can access the hypervisor
e.g. python resolve_conflict.py ece792@192.168.122.71,user@anotherIP



Side note:
Script to reset MAC address of a VM
python test_resetMac.py VM2-yk eth1 52:54:00:02:02:02