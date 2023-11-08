# writing the files in python:

f=open("2.txt","w")
f.write("he is nice person")
f.write("he is nice person")
f.write("he is nice person")
f.write("he is nice person")
f.close()


f=open("2.txt","a")
f.write("this will come at last")
f.close()

# with statement in file o/i

with open("2.txt","r")as f:
    a=f.read()
    print(a)