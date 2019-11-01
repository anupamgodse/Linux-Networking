sudo virsh destroy yjkamdarVM1
sudo virsh destroy yjkamdarVM2
sleep 5
sudo virsh undefine yjkamdarVM1
sudo virsh undefine yjkamdarVM2
sudo virsh net-destroy yjkamdar-netl3
sudo virsh net-undefine yjkamdar-netl3
sudo ovs-vsctl del-br netl3-br

