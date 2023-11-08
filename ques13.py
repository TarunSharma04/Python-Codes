# write a python program to fill in a letter template given below with name and date.

letter='''Dear <|name|>,
You are selected!
come meet us on 
<|date|>'''
name=input("enter the name: ")
date=input("enter the name: ")
letter=letter.replace("<|name|>",name)
letter=letter.replace("<|date|>",date)
print(letter)