  #normal function
'''
def sq_numbers(nums):
    l=[]
    for i in nums:
        l.append(i*i)
    return l

print(sq_numbers([1,2,3,4,5])) # [1,4,9,16,25]   
'''
# working with generator using yield


def sq_numbers(nums):
    for i in nums:
        yield(i*i)

res=sq_numbers([1,2,3,4,5])

print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
try:
    print(next(res))
except StopIteration:
    print('rey error ')
