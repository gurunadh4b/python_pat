'''from sample import *
print('creating object')
obj=sample(1,2)
print(obj)
print(obj._name)'''
'''del obj
print(obj.add())
print(obj.add_no(12))
'''
class aim:
    def __init__(self,no,name):
        self.no=no
        self.name=name
    def meth(self,name):
        print('this is method')
        print(self.name)
ob=aim(1,'uday')
ob.meth('uday')
print(ob)
