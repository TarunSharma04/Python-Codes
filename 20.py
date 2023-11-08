# oops=object oriented progrmming=this type of apporach to solve the code 
# makes the code looks well organised and can be reuseable.

''' pascal case== EmployeeName
camel case== employeename '''

# this is called as class
class AdmissionForm:

    def print(self):
        print("the college name is: ", self.clgname)
        print("the course in which you are enrolled: ", self.course)
        print("the semester in which you are currently present: ", self.semester)

# this is called as object
ayushapplication = AdmissionForm()

# this is another object
harryapplication=AdmissionForm()

harryapplication.clgname="dtu"
harryapplication.course="bsc"
harryapplication.semester="4th"
harryapplication.print()

ayushapplication.clgname = "dpgitm"
ayushapplication.course = "b.tech"
ayushapplication.semester = "3rd"
ayushapplication.print()


# pops=it is a type of apporach to implement in program which is also known as procedural oriented programming.
a = 12
b = 19
print("the sum of two number is:", a+b)
