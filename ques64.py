# create a class programmer for storing information of few programmers working at microsoft.

class programmer:
    company="microsoft"
    def __init__(self,name,salary,age,yoe,desgination):
        self.name=name
        self.age=age
        self.desgination=desgination
        self.salary=salary
        self.yoe=yoe
    def getdetails(self):
        print("The employee name is:",self.name)
        print("The employee's salary is(in us dollars):",self.salary)
        print("The employee's age is:",self.age)
        print("The employee year of experince in company is:",self.yoe)
        print("The employee desgination in company is:",self.desgination)

employee1=programmer("vikas",150,21,1,"assitant manager")
employee2=programmer("shubham",120,23,2,"ios developer")
employee3=programmer("ayush" ,200, 25, 5, "manager")
employee4=programmer("abhishek", 100, 25, 2, "android developer")
employee1.getdetails()
employee2.getdetails()
employee3.getdetails()
employee4.getdetails()