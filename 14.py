#1. while loop

print(" WRITE A PROGRAM TO PRINT 1 TO 50 USING WHILE LOOP.")
a = 1  #== initalization
while(a <= 50):#==>condition
    print(a)
    a =a + 1  #==iteration(a+=1)

i=1
while(i<=5):
 print("ayush")
 i+=1

#note: if we simply make an condition which never become false in the loop then we create a infinite loop.

print("write a program to print the content of the list using while loops.")
b=["harry",23,445,67,88,"ayush"]
j=0
while(j<len(b)):
    print(b[j])
    j+=1
print("else in while loop")
k=0
while(k<=10):
    print(k)
    k=k+1
else:
    print("this is the end point")        