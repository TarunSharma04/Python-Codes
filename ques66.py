#QUES=create a class attribute a; create an object from it and set a directly using
#object a=0.does this change bthe class attribute.
# ANS= sample attributes print his own value and object attributes prints it's own .

class sample:
    # this is class attribute
    a="ayush"

obj=sample()

# this is instance attribute
obj.a="harry"
print(obj.a)
print(sample.a)