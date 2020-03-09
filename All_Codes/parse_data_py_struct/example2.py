from ncclient import manager
from lxml import etree as ET

router = {"host": "ios-xe-mgmt-latest.cisco.com", "port": "10000",
          "username": "developer", "password": "C1sco12345"}

netconf_filter = """
 <filter>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>GigabitEthernet2</name>
    </interface>
  </interfaces>
  <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>GigabitEthernet2</name>
    </interface>
  </interfaces-state>
</filter>
"""

root = ET.Element("filter")
interfaces = ET.SubElement(root,"interfaces")
interfaces.set("xmlns","urn:ietf:params:xml:ns:yang:ietf-interfaces")
interface = ET.SubElement(interfaces,"interface")
name = ET.SubElement(interface,"name")
name.text = "GigabitEthernet2"

interfacesState = ET.SubElement(root,"interfaces-state")
interfacesState.set("xmlns","urn:ietf:params:xml:ns:yang:ietf-interfaces")
interface = ET.SubElement(interfacesState,"interface")
name = ET.SubElement(interface,"name")
name.text = "GigabitEthernet2"



with manager.connect(host=router["host"], port=router["port"], 
username=router["username"], password=router["password"], hostkey_verify=False) as m:
    # get the running config on the filtered out interface
    print('Connected')
    interface_netconf = m.get(netconf_filter)
    #interface_netconf = m.get(ET.tostring(root, encoding = "unicode"))
    print('getting running config')    

# lxml to parse XML string into ET objects
data = interface_netconf.data_ele

#Extract the interface name by index
name = data[0][0][0].text

#Extract the interface name by XPath query
name = data.xpath('.//nc:interfaces//nc:interface//nc:name', 
  namespaces={'nc':'urn:ietf:params:xml:ns:yang:ietf-interfaces'})[0].text

#Extract the description by index
description = data[0][0][1].text

#Extract the description by XPath query
description = data.xpath('.//nc:interfaces//nc:interface//nc:description', 
  namespaces={'nc':'urn:ietf:params:xml:ns:yang:ietf-interfaces'})[0].text

#Extract the packets in stats by XPath query
packetsIn = data.xpath('.//nc:interfaces-state//nc:interface//nc:statistics//nc:in-unicast-pkts', 
  namespaces={'nc':'urn:ietf:params:xml:ns:yang:ietf-interfaces'})[0].text

print("Start")
print(f"Name: {name}")
print(f"Description: {description}")
print(f"Packets In {packetsIn}")
