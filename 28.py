                #global variables

a = 12

def func():
    global a
    a = 14
    a = 15
    print(a)

print(a)
func()

            # ENUMERATE IN PYTHON

# old method to print item in list.
# i=0
# for item in list:
#   i=i+1
#   print("item number",i,"is",item)

# new method to print item from the list.
list = [12, 23, 4, 66, 78]
for i, item in enumerate(list):
    print("item number", i, "is", item)

                #List,set and dictionary COMPREHENSIONS

#old method
#l1=[1,2,3,4,5,6]
#l2=[]
#for item in l1:
#   l2.append(item*item)
#print(l2)

#new method
l1=[1,2,3,4,5,6]
l2=[i*i for i in l1]
print(l2)
d1={12:"a whole number",35:"a whole number",56:"a whole number",78:"a whole number",344:"a whole number"}
d2={i*i for i in d1}
print(d2)
s1={1,2,3,4}
s2={i*i for i in s1}
print(s2)