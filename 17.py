# recursion

# factorial of 5?
# 5!=5*4!
# factorial using for loops
n = 5
product = 1
for i in range(n):
    # (1*1=1)*(1*2=2)*(1*3=3)*(1*4=4)*(1*5=5)
    product = product*(i+1)
print(product)

# factorial using functions


def func_iter_fatorial(n):
    product = 1
    for i in range(n):
        product = product*(i+1)
    return product

print(func_iter_fatorial(5))

# factorial using recursion
# function calling itself
def func_factorial_recursive(n):
    if  n== 0 or n == 1:
        return 1
    else: 
        return n*func_factorial_recursive(n-1)
        
print(func_factorial_recursive(5))