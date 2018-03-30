import time
from threading import Thread
even_nos=[]
odd_nos=[]
div_nos=[]
def find_even(number):
    print('finding even number')
    for i in range(number):
        time.sleep(0.5)
        if i%2==0:
                print('even number is :',i)
        even_nos.append(i)
def find_odd(number):
    print('finding odd number')
    for i in range(number):
        time.sleep(0.5)
        if i%2!=0:
                print('odd number is:',i)
        odd_nos.append(i)
def find_divisible_by_5(number):
    print('finding divisible by 5 number')
    for i in range(number):
        time.sleep(0.5)
        if i%5==0:
                print('divisible by 5 is :',i)
        div_nos.append(i)

start_time=time.time()
t1=Thread(target=find_even,args=(20,))
t2=Thread(target=find_odd,args=(20,))
t3=Thread(target=find_divisible_by_5,args=(20,))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print(even_nos)
print(odd_nos)
print(div_nos)
end_time=time.time()

print('execution time is :',end_time-start_time)
