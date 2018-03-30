class sample:
    "this is the class operation"
    print('inside class')
    count=0
    _name='uday'   
    def __init__(self,a,b,c=30):
        self.a=a
        self.b=b
        self.c=c

    def add(self):
        s=self.a+self.b
        return s
    def add_no(self,x):
        s1=self.a+self.b+self.c+x
        return s1

if __name__=='__main__':
    print('=======inside main======')
    sam=sample(10,30)
    sum=sam.add()
    print('sum :',sum)
    print(sam.count)

    #get attr
    print(getattr(sam,'a'))
    print(sam.a)

    #set attr
    sam.a=100
    setattr(sam,'a',120)
    print(sam.add())

    #delete attr
    #delattr(sam,'a')
    #print(sam.add())

    print('=======outside main========')
    sam=sample(10,20)
#Built in class attributes
    print('Dict :',sam.__dict__)
    sam2=sample(100,200)
    print('dict :',sam2.__doc__)
    print('doc :',sam.__doc__)
    print('name :',sample.__name__)
    print('module :',sample.__module__)
    print('base class :',sample.__bases__)
    print(__name__)
