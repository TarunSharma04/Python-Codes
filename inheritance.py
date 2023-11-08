class parent1:
    def __init__(self,name,marks,rollno):
        self.name=name
        self.marks=marks
        self.rollno=rollno
    def getdetails(self):
        print("the employee name is",self.name)
        print("the employee's company name is",self.company)
        print("the employee's age is",self.age)
class parent2:  
    def __init__(self,sec,branch):
        self.branch=branch
        self.sec=sec
    def getdetails(self):
        print("the employee name is",self.name)
        print("the employee's company name is",self.company)
        print("the employee's age is",self.age)
class parent3:
    def __init__(self,age):
        self.age=age
    def getdetails(self):
        print("the employee's age is",self.age)