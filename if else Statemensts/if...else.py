# The if statement can have an optional else clause.

#  if boolean_expression:
#       statement(s)
#  else:
#       statement(s)

# Working:

# 1. If the boolean expression evaluates to True, the body of the statement is executed.
# 2. If the boolean expression evaluates to False, the body of the else statement is executed.

# Example:

number = -4
if number > 0:
    print("The number is positive")
    print("The body of if statement is executed")
else:
    print("The number is negetive")
    print("The body of else statement is executed")

number2 = 5
if number2 > 0:
    print("The number is positive")
    print("The body of if statement is executed")
else:
    print("The number is negetive")
    print("The body of else statement is executed")