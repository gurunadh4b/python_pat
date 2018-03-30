import json
import xmltodict
 
with open('output.json', 'r') as f:
    jsonString = f.read()
 
print(jsonString)
 
xmlString = xmltodict.unparse(json.loads(jsonString))
 
print(xmlString)
 
with open('output.xml', 'w') as f:
    f.write(xmlString)
