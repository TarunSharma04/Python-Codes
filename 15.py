# 2. for loop

list = ["bannana", "apple", "grapes", "avacado", "watermelon"]
for item in list:
    print(item)

# range function in python
print('topic-range function')
for i in range(1, 8, 2):
    # For i in range(start,stop,step-wise)
    print(i)

# for loop with else
print("topic-for loop with else")
for i in range(1, 10):
    print(i)

else:
    print("this is the end point")

# the break statement
print("break statement")
for i in range(10):
    print(i)
    if(i == 6):
        break

# continue statement
print("continue statement")
for j in range(10):

    if(j==6):
     continue
    print(j)

# pass statement
#IndentationError: expected an indented block after 'for' statement
# if we use pass statement it will not show an error.
print("pass statement")
for i in range(10):
    pass