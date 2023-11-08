#__init__() constructors

class comp:
    def __init__(self,name,roll,per):
        self.name=name
        self.roll=roll
        self.per=per
    
    def getdetails(self):
        print(self.name)
        print(self.roll)
        print(self.per)

        
ayush=comp("ayush",155,14)
ayush.getdetails()