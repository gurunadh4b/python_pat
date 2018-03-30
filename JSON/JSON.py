family={}
family['uday']={
        'name':'uday',
        'sal':25000,
        'address':'vizag'
        }
family['chanti']={
         'name':'chanti',
         'sal':20000,
         'address':'rajahmundry'
         }

import json
s=json.dumps(family)
print(s)
type(s)
with open('jsontextfile','w') as f:
    f.write(s)
