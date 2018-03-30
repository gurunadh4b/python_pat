num = int(input('enter value for row :'))
'''row = 0
while row<num:
    space = num-row-1
    while space>0:
        print(end="")
        space = space-1
    star = row+1
    while star>0:
        print("*",end="")
        star = star-1
    row = row+1
    print()
''' 
'''for i in range(1,num):
    for j in range(0,num-i-1):
        print(end ="")
    for j in range(0,i+1):
        print('*',end='')
    print()
'''
for i in range(1,num):
    for j in range(num+1):
        print("",end='')
    for j in range(1,i):
        print(j,end='')
    for i in range(i,0,-1):
        print(i,end='')
    
    print('\n')
