from ncclient import manager
import xmltodict

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

netconf_filter_obj = {
  "filter":{
    "interfaces":{
      "interface":{
        "name":"GigabitEthernet2"
      },
      "@xmlns":"urn:ietf:params:xml:ns:yang:ietf-interfaces"
    },
    "interfaces_state":{
      "interface":{
        "name":"GigabitEthernet2"
      },
      "@xmlns":"urn:ietf:params:xml:ns:yang:ietf-interfaces"     
    }
  }
}

netconf_filter_xml = xmltodict.unparse(netconf_filter_obj)

with manager.connect(host=router["host"], port=router["port"], 
username=router["username"], password=router["password"], hostkey_verify=False) as m:
    # get the running config on the filtered out interface
    print('Connected')
    interface_netconf = m.get(netconf_filter)
    #interface_netconf = m.get(netconf_filter_xml)
    print('getting running config')    

# XMLTODICT for converting xml output to a python dictionary
interface_python = xmltodict.parse(interface_netconf.xml)["rpc-reply"]["data"]

name = interface_python['interfaces']['interface']['name']['#text']

config = interface_python["interfaces"]["interface"]
op_state = interface_python["interfaces-state"]["interface"]

print("Start")
print(f"Name: {config['name']['#text']}")
print(f"Description: {config['description']}")
print(f"Packets In {op_state['statistics']['in-unicast-pkts']}")
