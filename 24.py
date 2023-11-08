#1.single inheritance
class employee:
    a=34
class programmer(employee):
    b=32

ayush=programmer()
deepanshu=employee()

print(ayush.a,"dervied(base) class")
print(ayush.b,"dervied class")
print(deepanshu.a,"base class")

# this line through an eror=AttributeError:'employee' object has no attribute 'b'
#print(em.b)

#2.multi inheritance
class parent1:
    a=36
class parent2:
    b=23
class parent3:
    c=89
class chlid(parent1,parent2,parent3):
    d=45


ch=chlid()
par1=parent1()
par2=parent2()
par3=parent3()
print(ch.a,"chlid(parent1) class")
print(ch.b,"chlid(parent2) class")
print(ch.d,"chlid class")
print(ch.c,"chlid(parent3) class")

# 3.mutlilevel inheritance

class parent:
    a=99
class chlid1(parent):
    b=68
class chlid2(chlid1,parent):
    c=90

ch1=chlid1()
ch2=chlid2()

print(ch2.a,"chlid2(parent) class")
print(ch2.b,"chlid2(chlid1) class")
print(ch2.c,"chlid2 class")

#print(ch1.c) #it will show an error =AttributeError: 'chlid1' object has no attribute 'c'