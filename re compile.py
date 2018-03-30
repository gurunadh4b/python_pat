'''import re
s='yes python is programming language'
print(s)
pat=re.compile('python')
print(pat.search(s))
'''
import re
'''s='python is scripting language'
k=re.sub('python','java',s)
print(k)
print(s)'''

'''
a='100 guru 100'
b='guru 100 guru'
m=re.sub('\d+','hi',a) #hi guru hi
n=re.sub('\w+','100',b)# 100 100 100
print(m) 
print(n)
'''
'''
a='100 guru 200 300'
print(re.split('\d\s',a))
'''

'''
a='28uday26guru24schanti'
print(re.findall('\d',a))
print(re.findall('\D',a))
'''
'''
f=open('findallfile.txt')
lines=f.readlines()
empty=[]
for line in lines:
    print(line)
    l=re.findall('\d+',line)
    empty.extend(l)
    print(empty)'''










