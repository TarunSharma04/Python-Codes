#method overloading
#you have to install mutiple dispatch library
from multipledispatch import dispatch
class A:
    @dispatch(int,int)
    def product(a,b):
        c=a*b
        print(c)
    @dispatch(int,int,int)
    def product(d,e,f):
        y=d*e*f
        print(y)
    @dispatch(float,float,float)
    def product(h,i,j):
        k=h*i*j
        print(k)
E=A()
E.product(10,15)
E.product(10,20,30)
E.product(4.7,8.9,6.8)



# oprerators overloading in python
'''class employee:
    def __init__(self,a,name):
       self.a=a
       self.name=name
    def __add__(self,obj):
        return self.a+obj.a
    def __str__(self):
        return self.name
    def __len__(self):
        return self.a
a=employee(12,"ayush")
b=employee(6,"harry")
print(a+b)
print(a,b)
print(len(a))
print(len(b))'''

#addition operator overloading

class A:
    def __init__(self,a):
        self.a=a
    def __add__(self,o):
        return self.a+o.a   
ob1=A(1)
ob2=A(2)
ob3=A("WELCOME")
ob4=A("dpgitm")
print(ob1+ob2)
print(ob3+ob4)

# mutiply operator overloading
class A:
    def __init__(self,a):
        self.a=a
    def __mul__(self,o):
        return self.a*o.a   
ob1=A(1)
ob2=A(2)
ob3=A(10)
ob4=A(20)
print(ob1*ob2)
print(ob3*ob4)

#greater than overloading
class A:
    def __init__(self,a):
        self.a=a
    def __gt__(self,o):
        if(self.a>o.a):
            return self.a
        return o.a

ob1=A(1)
ob2=A(3)
ob3=A("welcome")
ob4=A("Dpgitm")
print(ob1>ob2)
print(ob3>ob4)

#less than overloading
class A:
    def __init__(self,a):
        self.a=a
    def __lt__(self,o):
        if(self.a<o.a):
            return self.a
        return o.a

ob1=A(1)
ob2=A(3)
ob3=A("welcome")
ob4=A("Dpgitm")
print(ob1<ob2)
print(ob3<ob4)