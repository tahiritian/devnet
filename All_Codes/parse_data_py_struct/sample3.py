import xmltodict

#Get the XML file data
stream = open('sample.xml','r')

#Prase the XML file into an 'OrderedDict'
xml = xmltodict.parse(stream.read())

for e in xml["People"]["Person"]:
    print(e)

