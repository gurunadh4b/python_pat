f=open('jsontextfile.txt','r')
s=f.read()
print(s)
print(type(s))

import json
family=json.loads(s)
print(family)
print(type(family))
