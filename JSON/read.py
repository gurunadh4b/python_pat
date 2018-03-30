'''f=open('newfile.txt','r')
r=f.readlines()
print(r)
'''

'''with open('newfile.txt','r') as file:
    s=file.read()
    print(s)
'''

with open('newfile.txt','a') as file:
    s=file.write('\nyuvraj\ndhoni\nkohli\nzaheer\naswin')
    print(s)
