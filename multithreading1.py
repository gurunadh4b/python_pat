import time
def find_even(number):
    print('finding even number')
    for i in range(number):
        time.sleep(0.5)
        if i%2==0:
                print('even number is :',i)
def find_odd(number):
    print('finding odd number')
    for i in range(number):
        time.sleep(0.5)
        if i%2!=0:
                print('odd number is:',i)
def find_divisible_by_5(number):
    print('finding divisible by 5 number')
    for i in range(number):
        time.sleep(0.5)
        if i%5==0:
                print('divisible by 5 is :',i)

start_time=time.time()
find_even(20)
find_odd(20)
find_divisible_by_5(20)
end_time=time.time()

print('execution time is:',end_time-start_time)
