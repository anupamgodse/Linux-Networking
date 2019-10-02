import sys
import libvirt

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', file=sys.stderr)
    exit(1)

hostname = conn.getHostname()
vcpus = 4
info = conn.getInfo()
htype = conn.getType()
isAlive = conn.isAlive()
isSecure = conn.isSecure()
version = conn.getVersion()
freeMem = conn.getFreeMemory()

print('Hostname: '+str(hostname)+'\nvcpus: '+str(vcpus)+'\ninfo: '
        +str(info)+'\ntype: '+str(htype)+'\nisAlive: '+str(isAlive)+
        '\nisSecure: '+str(isSecure)+'\nversion: '+str(version)+
        '\nfreeMem: '+ str(freeMem))

conn.close()
exit(0)
