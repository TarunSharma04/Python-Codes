# The if...elif...else statement allows us to make a choice from two options. If you need to make a choice from more the 2 options,
# you can use the elif part in the if...else statement.
# Syntax:
#       if boolean_expression1:
#         statement(s)
#       elif boolean_expression2:
#         statement(s)
#       else:
#         statement(s)12

# NOTE: There can be 0 or more elif parts. By the way, elif is short for else if.

# Example:

num1 = 0
num2 = 2
num3 = -3
if num1> 0:
    print("Positive number")
elif num1 == 0:
    print("Zero")
else:
    print("Negetive number")

if num2> 0:
    print("Positive number")
elif num2 == 0:
    print("Zero")
else:
    print("Negetive number")
    
if num3> 0:
    print("Positive number")
elif num3 == 0:
    print("Zero")
else:
    print("Negetive number")