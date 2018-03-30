import re
s='python is programming language'
pattern='programming'
if re.match(pattern,s):
    print('yes pattern matched')
else :
    print('sorry pattern doesnt match')



import re
s='python is scripting language'
pattern='.*scripting'
if re.match(pattern,s):
    print('yes pattern matched')
else:
    print('sorry doesnt matched')
