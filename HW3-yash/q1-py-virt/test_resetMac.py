# Listing all MACs and IPs of VMs
import sys
import libvirt
import xml.etree.ElementTree as ET
import time
import random

def resetMac(domName,iface,curr_mac):
    dom = conn.lookupByName(domName)
    dom_xml = dom.XMLDesc(0)
    #new_mac="52:54:00:%02x:%02x:%02x" % (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
    new_mac="52:54:00:11:8b:fd"
    xml_root = ET.XML(dom_xml)
    interfaces = xml_root.find('devices').findall('interface')
    for interface in interfaces:
        mac_tag = interface.find('mac')
        if mac_tag.attrib['address'] == curr_mac:
            print('Resetting')
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

conn = libvirt.open('qemu:///system')
resetMac(sys.argv[1],sys.argv[2],sys.argv[3])
#resetMac('VM2-yk','eth1','52:54:00:4b:ad:6d')