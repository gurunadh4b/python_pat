class sample1:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print('first add')
        return self.a+self.b
        
class sample2(sample1):
    def sub(self):
        print('second add')
        return self.a+self.b
        
obj1=sample1(10,20)
print(obj1.add())

obj2=sample2(20,30)
print(obj2.add())
print(obj2.sub())

print(dir(obj1),dir(obj2))
