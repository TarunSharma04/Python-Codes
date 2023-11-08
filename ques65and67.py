#ques=write a class calculator capable of finding square,cube,and square root of a number.
#ques=use the static method to greet user with hello.


class calculator:
     def square(self,num):
        sq=num*num
        return sq
     def cube(self,num):
        cub=num*num*num
        return cub
     def squareroot(self,num):
        sqrt=(num)**(1/2)
        return sqrt
     @staticmethod
     def greet():
        print("HELLO")

b=calculator()


print(b.square(12))
print(b.cube(12))
print(b.squareroot(12))
b.greet()