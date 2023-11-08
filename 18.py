# file i/o
# reading the file in python:

# this will open file in r mode
f=open('1.txt','r')

#it will read contents
# if we not write any mode default it takes "r" as mode
a=f.read()

# it will prints the value stored in a.
print(a)

#close the file
f.close()
#it will reads first two charcter.
#data=f.read(2)

f=open('1.txt')

# read first line
b=f.readline()
print(b)

# read second line
b=f.readline()
print(b)

# read thrid line
b=f.readline()
print(b)

# read fourth line
b=f.readline()
print(b)

f.close()