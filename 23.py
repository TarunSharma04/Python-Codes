#__init__() constructors==>instance class

class employee:
    def __init__(self,name,age,company):
        self.name=name
        self.age=age
        self.company=company
    
    def getdetails(self):
        print("the employee name is",self.name)
        print("the employee's company name is",self.company)
        print("the employee's age is",self.age)

        
ayush=employee("ayush",19,"google")
ayush.getdetails()