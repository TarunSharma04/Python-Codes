# super method,class method,property decorators and setters property
class parent:
    a = 99

    def __init__(self):
        print("parent")


class chlid1(parent):
    b = 8

    def __init__(self):
        super().__init__()
    print("chlid1")
    print("hi how are you")


class chlid2(chlid1):
    c = 90

    def __init__(self):
        super().__init__()
    print("chlid2")


ch2 = chlid2()

print(ch2.a)
print(ch2.b)
print(ch2.c)

# supermethod=when we apply super method in second chlid class it will gives us access to the second chlid(parent) 
# class method and variables.
# when we apply super method in second chlid(parent) class it will gives us access to the 
# parent class method and variables.

#class method= this is also a way to make changes in class attributes.
#property decorators= it will make class attributes as a function which we can simply print it out(print(frsh.name)).
#setters property= if we have to make changes in class attributes we can done it easliy by creating a function
#which takes the value from the user and store it,and when required simply print the changed class attributes.
#{frsh.name = 20
#print(frsh.name)}

class fresher:
    a = 12
    b = 13
    c = 19

    @classmethod
    def setattr(cls, a, b, c):
        cls.a = a
        cls.b = b
        cls.c = c

    @property
    def name(self):
        return self.a

    @name.setter
    def name(self, value):
        self.a = value


frsh = fresher()
print(fresher.a)
print(fresher.b)
print(fresher.c)

frsh.setattr(18, 67, 78)

print(fresher.a)
print(fresher.b)
print(fresher.c)

print(frsh.name)
frsh.name = 20
print(frsh.name)