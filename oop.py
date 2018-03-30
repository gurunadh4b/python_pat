class sample:
    print('inside class')
    count=0
    def __init__(self,a,b):
        print('constructor')
        self.a=a
        self.b=b
    def add(self):
        q=self.a+self.b
        return q
o=sample(10,20)
sum=o.add()
print(sum)
print(o.count)

print(getattr(o,'b'))
