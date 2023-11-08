from functools import reduce

# map=it applies a function(square) to all the items in an input list.

sqr = lambda a:a**(1/2)
l = [121, 144, 169, 196, 256, 289, 324, 361, 400]
m = list(map(sqr, l))
print(m)

# filter=create a list of items for which the function returns true

greater=lambda a: a > 280
l = [121, 144, 169, 196, 256, 289, 324, 361, 400]
n = list(filter(greater, l))
print(n)

# reduce=it applies a rolling computation to sequential pair of elements

sum=lambda a,b:a+b
l = [1, 2, 3, 4]
p = reduce(sum, l)
print(p)

#pratice set=ques77 start
