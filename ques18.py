# write a program to accept marks of the students and display them in a sorted manner.
# ques 19 in repl or windows powershell.
m1=int(input("enter the marks of first student: "))
m2=int(input("enter the marks of second student: "))
m3=int(input("enter the marks of thrid student: "))
m4=int(input("enter the marks of fourth student: "))
m5=int(input("enter the marks of fifth student: "))
m6=int(input("enter the marks of sixth student: "))
marks=[m1,m2,m3,m4,m5,m6]
marks.sort()
print(marks)