# Let's learn with an example.

print(55 - 4 * 2)

# Output is 47 not 102. It's because the order operator precedence of * is higher than -, means * operator is carried out before -.

print((55-4)*2)

# Now output is 102. because () has the highest order of operator precedence. Hence (55-4) is carried out first.

# Operator Precedence List:

# 1. ()
# 2. **
# 3. +x, -x
# 4. *, /, //, %
# 5. +, -