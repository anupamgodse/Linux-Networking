Ensure Guest-agent is installed in all VMs, if not then install using
yum install qemu-guest-agent

Verify from Hypervisor:
virsh qemu-agent-command VM1-yk '{"execute":"guest-network-get-interfaces"}'