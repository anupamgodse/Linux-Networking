# Listing all MACs and IPs of VMs
import sys
import libvirt

def printInfo(VMinfo):
    for vm in sorted (VMinfo.keys()) :  
        print(VMinfo[vm]['name'])
        for iface in VMinfo[vm]['name'].keys():
            print(iface,VMinfo[vm][iface])

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
        if(mac_address!='00:00:00:00:00:00'):
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
MACs=[]
if domainIDs == None:
    print('Failed to get a list of domain IDs')
for dom_id in domainIDs:
    try:
        loadInfo(dom_id)
    except Exception as e:
        pass
printInfo(VMinfo)

