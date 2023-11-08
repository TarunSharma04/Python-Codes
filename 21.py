# class attributes= those attributes which belongs only to the class .
# object attributes= those attributes which belongs only to the object.

class Employee:
    company="google"
    salary=60

ayush=Employee()
harry=Employee()

# object attributes which may differ from object to object.
ayush.salary=300000
harry.salary=50
print(ayush.salary)
print(harry.salary)

# class attributes are same for all the object only when instance attributes is not given.
print(ayush.company)
print(ayush.salary)
print(harry.salary)
print(harry.company)

# it will change the class attributes
Employee.company="youtube"
print(ayush.company)
print(harry.company)


'''ques=which will take more prefernce a class attributes or object attributes?
         ans=object attributes will take more prefernce than class attributes.
    when instance attruibutes is not given then only it takes value from class attributes.
         if both the class and object attributes are not given then only it will show an error
   (AttributeError: 'Employee' object has no attribute 'address')  '''