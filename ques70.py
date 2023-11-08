# create a clas pets from a class animals and further create class dog
# from pets.add a method bark to class dog.


class Pets:
    a=145 
    b=356


class animals(Pets):
 a=12 
 b=13


class dog(animals):
    def print(self):
        print("bauh bauh")
    
germanleopard=dog()
germanleopard.print()
