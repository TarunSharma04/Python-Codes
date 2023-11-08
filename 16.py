# functions
# ways to print functions
#1.function with arguements
def percent(marks):
    p=((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
    return p

marks = [72, 74, 85, 77]
marks1 = [45, 55, 67, 68]
percentage=percent(marks)
percentage2=percent(marks1)
print("the percentage of marks is",percentage,"and the second percentage is",percentage2 )

# ques=write a program to greet usee with a "good day".
# we used function call here
#2.function with print function and default parameter value
def greet(name="stranger"):
    print("good day,",name)
       
greet("ayush")
greet()

# here we give value to function and then print it.
#3.function by return value
def mysum(num1,num2):
    #u=(num1+num2)
    #return u
    return(num1+num2)
s=mysum(6,12)
print(s)
  
