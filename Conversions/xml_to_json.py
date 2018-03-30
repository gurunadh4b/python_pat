import json
import xmltodict
 
with open("myfile.xml", 'r') as f:
    xmlString = f.read()
 
print(xmlString)
     
jsonString = json.dumps(xmltodict.parse(xmlString), indent=1)
 
print(jsonString)
 
with open("output.json", 'w') as f:
    f.write(jsonString)
