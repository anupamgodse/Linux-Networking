# Listing all MACs and IPs of VMs
import sys
import libvirt

def loadInfo(domainID):
    dom = conn.lookupByID(domainID)
    currInfo=dict()
    interfaces=[]
    domName=dom.name()

    ifaces = dom.interfaceAddresses(libvirt.VIR_DOMAIN_INTERFACE_ADDRESSES_SRC_AGENT, 0)

    print("The interface IP addresses:")
    for (name, val) in ifaces.iteritems():
        if val['addrs']:
            for ipaddr in val['addrs']:
                if ipaddr['type'] == libvirt.VIR_IP_ADDR_TYPE_IPV4:
                    print(ipaddr['addr'] + " VIR_IP_ADDR_TYPE_IPV4")
                elif ipaddr['type'] == libvirt.VIR_IP_ADDR_TYPE_IPV6:
                    print(ipaddr['addr'] + " VIR_IP_ADDR_TYPE_IPV6")

    currInfo['name']=dom.name()
    currInfo['interfaces']=interfaces
    VMinfo[domainID]=currInfo


conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', file=sys.stderr)
    exit(1)
# domainIDs = conn.listDomainsID()
# VMinfo=dict()
# if domainIDs == None:
#     print('Failed to get a list of domain IDs', file=sys.stderr)
# #for id in domainIDs:
loadInfo(121)