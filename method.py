class student:
    school="euro"
    def __init__(self,n1,n2,n3):
        self.n1=n1
        self.n2=n2
        self.n3=n3
    @classmethod
    def info(cls):
        return cls(school)
a=student(1,2,3)
print(a.info())