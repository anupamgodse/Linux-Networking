sudo virt-clone --original sampleVM -n cvm --auto-clone
sudo virt-clone --original sampleVM -n rvm --auto-clone
sudo virt-clone --original sampleVM -n svm1 --auto-clone
sudo virt-clone --original sampleVM -n svm2 --auto-clone

virsh attach-interface --domain cvm --type network --source public-net --model virtio --config --live
virsh attach-interface --domain rvm --type network --source public-net --model virtio --config --live
virsh attach-interface --domain rvm --type network --source private-net --model virtio --config --live
virsh attach-interface --domain svm1 --type network --source private-net --model virtio --config --live
virsh attach-interface --domain svm2 --type network --source private-net --model virtio --config --live
