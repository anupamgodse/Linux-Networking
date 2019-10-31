Steps to run:
python p1.py
python p2.py



Notes:Ensure Guest-agent is installed in all VMs, if not then install using
yum install qemu-guest-agent

Verify from Hypervisor:
virsh qemu-agent-command VM1-yk '{"execute":"guest-network-get-interfaces"}'

Another approach would be to fetch the IP from the dnsmasq leases file on the hypervisor (/var/lib/misc/dnsmasq.leases),
but my approach would fetch even the static IPs set in the guest VM.

