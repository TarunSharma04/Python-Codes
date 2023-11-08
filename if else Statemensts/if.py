# The syntax of if statement is:

#  if boolen expression:
#      statement(s)
#  The if statement evaluates the boolen expression.
#  1. If the boolean expression evaluates to True, the body of the if satement is executed.
#  2. If the boolean expression evaluates to False, the body o fthe if statement is skipped.

#  NOTE: In Python, identation is used to define a block of code. The body if the if statement is also determined through identation.

# EXAMPLE:

number = 10

if number > 0:
    print("The number is positive.")
print("This is always executed.")

# The statement  print("This is always executed.")  is outside the body of the if statement. Hence, it is always executed.

number2 = -2

if number2 > 0:
    print("The number is positive.")
print("This is always executed")

# Here no.2 > 0 evaluates false because -2 > 0 is False. Hence, the body of if statement  print("The number is positive.")  is not executed.