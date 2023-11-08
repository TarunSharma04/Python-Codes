# We can have an if ...else statement inside another if...else statement. This is callled nesting in computer programming.

# Example:

num = float(input("Enter a number:"))
if num >= 0:

    if num == 0:
        print("The number is zero")
    else:
        print("The number is positive")
else:
    print("The number is negetive")