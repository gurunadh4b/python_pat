import re
'''ip='354.2.4.20'
if re.match('[0-5]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}',ip):
    print('valid ip address')
else:
    print('invalid ip address')
'''

ip='254.4.5.8'
if re.match('^(([0-9]|([1-9][0-9])|(1[0-9][0-9])|(2[0-4][0-9])|(25[0-5]))\.){3}([0-9]|([1-9][0-9])|(1[0-9][0-9])|(2[0-4][0-9])|(25[0-5]))$',ip):
    print('valid ip address')
else:
        print('invalid ip address')
