import re
n='100 test 200 guru'
m=re.search('((\d+) (\D+) (\d+) (\D+))',n)
if m:
    print(m.group())
    print('1st match is: ',m.group(0))
    print('2nd match is: ',m.group(1))
    print('3rd match is: ',m.group(2))
    print('4th match is: ',m.group(3))
    print('5th match is: ',m.group(4))
    print('4th match is: ',m.groups())
