import sys
import libvirt
from xml.dom import minidom

domName = 'angodseVM1'

conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', file=sys.stderr)
    exit(1)

dom = conn.lookupByName(domName)
if dom == None:
    print('Failed to find the domain '+domName, file=sys.stderr)
    exit(1)

id = dom.ID()
if id == -1:
    print('The domain is not running so has no ID.')
else:
    print('The ID of the domain is ' + str(id))

uuid = dom.UUIDString()
print('The UUID of the domain is ' + uuid)

type = dom.OSType()
print('The OS type of the domain is "' + type + '"')

flag = dom.hasCurrentSnapshot()
print('The value of the current snapshot flag is ' + str(flag))

#name = dom.hostname()
#print('The hostname of the domain  is ' + str(name))

state, maxmem, mem, cpus, cput = dom.info()
print('The state is ' + str(state))
print('The max memory is ' + str(maxmem))
print('The memory is ' + str(mem))
print('The number of cpus is ' + str(cpus))
print('The cpu time is ' + str(cput))

conn.close()
exit(0)
