import re
n='100 test 200'
m=re.search('(\d+) (\D+) (\d+)',n)
if m:
    print(m.group())
