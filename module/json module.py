json_data='{"employee_details":{"employ1":{"name":"uday","id":10},"employ2":{"name":"chanti","id":11}}}'



'''json_data='{"Family":{"Brother1":{"name":"uday","sal":25000,"address":"vizag"},"Brother3":{"name":"chanti","sal":18000,"address":"rajahmundry"}}}'
'''
import json
json_dict=json.loads(json_data)
print(json_dict)
print(type(json_dict))
print(type(json_data))
