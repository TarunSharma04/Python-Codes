# expection handling in python
'''by this try method ,this does not effect on the program it will just print the errorin it= print(e)'''

try:
    print("this is  Akki Sharma's PC")
    a = int(input("enter the first number:"))
    b = int(input("enter the second number:"))
    print(a+b)

except ValueError:
    print("your program has a value error")

except Exception as e:
    print("this error will occur=", e)

    # try with else clause=only execute when try statement suceessfully terminated.
else:
    print("when there are no error in this program then i will print")
    for i in range(1, 11):
        print(a, "X", i, "=", a*i)

    #try with finally= excute regardless of error or function returning
finally:
    print(" i will excute regardless of program error")
    for i in range(1,50):
        print(i)

if __name__=="__main__":
  print("main") 