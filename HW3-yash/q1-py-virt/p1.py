# Listing all MACs and IPs of VMs
import sys
import libvirt
import xml.etree.ElementTree as ET
import time
import random

def resetMac(domName,iface,curr_mac):
    dom = conn.lookupByName(domName)
    dom_xml = dom.XMLDesc(0)
    new_mac="52:54:00:%02x:%02x:%02x" % (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))

    xml_root = ET.XML(dom_xml)
    interfaces = xml_root.find('devices').findall('interface')
    for interface in interfaces:
        mac_tag = interface.find('mac')
        if mac_tag.attrib['address'] == curr_mac:
            mac_tag.attrib['address']=new_mac
    #xml_tree.write('/etc/libvirt/qemu/'+dom.name()+'.xml')
    xml_str=ET.tostring(xml_root)
    dom_file=open("/etc/libvirt/qemu/"+dom.name()+".xml",'wb')
    dom_file.write(xml_str)
    dom_file.close()
    dom.destroy()
    conn.defineXML(xml_str)
    if dom.isActive() != True: 
        dom.create()

def resolveConflicts(VMinfo):
    for vm in sorted (VMinfo.keys()) :
        interfaces=VMinfo[vm]['interfaces']
        for iface in interfaces.keys():
            curr_mac=interfaces[iface]['mac_address']
            if curr_mac in MACs:
                new_mac=resetMac(VMinfo[vm]['name'],iface,curr_mac)
                interfaces[iface]['mac_address']=new_mac
            else:
                MACs.append(curr_mac)

def printInfo(VMinfo):
    for vm in sorted (VMinfo.keys()) :  
        print(VMinfo[vm]['name'])
        interfaces=VMinfo[vm]['interfaces']
        for iface in interfaces.keys():
            print(iface,interfaces[iface])

def loadInfo(domainID):
    dom = conn.lookupByID(domainID)
    currInfo=dict()
    interfaces=dict()
    domName=dom.name()
    
    ifaces=[]
    try:
        ifaces = dom.interfaceAddresses(libvirt.VIR_DOMAIN_INTERFACE_ADDRESSES_SRC_AGENT, 0)
    except:
        #backup in case agent is not installed
        ifaces = dom.interfaceAddresses(libvirt.VIR_DOMAIN_INTERFACE_ADDRESSES_SRC_LEASE)

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

def libvirt_callback(userdata, err):
    pass

libvirt.registerErrorHandler(f=libvirt_callback, ctx=None)
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
    loadInfo(dom_id)
printInfo(VMinfo)
resolveConflicts(VMinfo)
printInfo(VMinfo)

