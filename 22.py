# self parameter, static method 

class books:
    
    def print(self):
        print("number of page in books:", self.pages)

    @staticmethod
    def greet():
       print("hello sir,how are you")

rdsharma = books()
slarora =books()

rdsharma.pages = 450
slarora.pages = 670

rdsharma.price=1100
slarora.price=1200

print(rdsharma.price)
print(slarora.price)

# this is for self parameter=> slarora.pages()=employee.pages(slarora)
rdsharma.print()
slarora.print()

# this is for static method
rdsharma.greet()
slarora.greet()

# when we not use self argument with function which is present in class it show an error written below=>
# TypeError: books.print() takes 0 positional arguments but 1 was given

# when we use self aruement with static method it will show an error.
#TypeError: books.greet() missing 1 required positional argument: 'self'