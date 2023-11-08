#operators in python

print("arthmetic operators")
a = 12
b = 6
print("a+b = ", a+b)
print("a-b = ", a-b)
print("a*b = ", a*b)
print("a/b = ", a/b)

print("assigment operators") 
c=13
d=10
print(c,d)
c += 5
d -= 10
print(c,d)

print("comparsion operators") 
e=4
f=2
print(e==f)
print(e<f)
print(e>f)
print(e<=f)
print(e>=f)
print(e!=f)

print("logical operators") 
g=1
h=7

''' in "and"==if both the operation are correct 
 then only it will print true'''

print(g>h and g<=h)

''' in "or"==if one of the operation is true then 
it will print true'''

print(g>h or g<=h)

''' in "not"== it will reverse the condition meaning 
if it is true then print it false 
if it is false then print true'''

print(not(g<h))
