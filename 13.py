#conditional statements/expressions
#1.if else statements

a=22
if(a>23):
    print("a is greater than 23.")
    # this will not execute because the value of a is 22 and 
    # this statement is saying that a is greater than 23 or not.
else:
    print("a is lesser than 23.")
    # this will execute because the value of a is 22 and 
    # this statement is saying that a is lesser than 23 or not.

# 2.else if statements 
b=int(input("enter the number: "))

if(b<10):
    print("the number is less than 10.")
elif(b<20):
    print("the number is less than 20.")
elif(b<30):
    print("the number is less than 30.")
else:
    print("the number is greater than 10,20 and 30.")

# quick quiz
# ques= write a program to print yes when the age entered by the user is greater than or equal to 18.
age=int(input("enter the age: "))
if(age>=18):
    print("Yes")
else:
    print("No")
    # logical and relational operators
d=12
e=14
print(d>=e and e>=d)
print(d>=e or e>=d)  
print(not(d>=e))
print(d==e)
print(d<=e)