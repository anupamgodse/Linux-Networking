# Listing all MACs and IPs of VMs
import sys
import libvirt

def loadInfo(domainID):
    dom = conn.lookupByID(domainID)
    currInfo=dict()
    interfaces=dict()
    domName=dom.name()

    ifaces = dom.interfaceAddresses(libvirt.VIR_DOMAIN_INTERFACE_ADDRESSES_SRC_AGENT, 0)

    for (name, val) in ifaces.iteritems():
        mac_address=val['hwaddr']
        ip_address=None
        if val['addrs']:
            for ipaddr in val['addrs']:
                if ipaddr['type'] == libvirt.VIR_IP_ADDR_TYPE_IPV4:
                    ip_address=ipaddr['addr']
        if ip_address:
            interfaces[name]={'mac_address':mac_address,'ip_address':ip_address}
        else:
            interfaces[name]={'mac_address':mac_address,'ip_address':None}

    currInfo['name']=dom.name()
    currInfo['interfaces']=interfaces
    VMinfo[domainID]=currInfo


conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system')
    exit(1)
domainIDs = conn.listDomainsID()
VMinfo=dict()
if domainIDs == None:
    print('Failed to get a list of domain IDs')
for dom_id in domainIDs:
    try:
        loadInfo(dom_id)
    except:
        print("An exception occurred")
print(VMinfo)