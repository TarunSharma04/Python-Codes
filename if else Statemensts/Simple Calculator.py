print("What operation do you want?")
n1 = float(input("Enter first number:"))
operator = input("Enter either +, -, * or /:")
n2 = float(input("Enter second number:"))
if operator == '+':
    print(n1, operator, n2, "=", n1+n2)

elif operator == '-':
    print(n1, operator, n2, "=", n1-n2)
elif operator == '*':
    print(n1, operator, n2, "=", n1*n2)
elif operator == '/':
    print(n1, operator, n2, "=", n1/n2)
else:
    print("Invalid operator")