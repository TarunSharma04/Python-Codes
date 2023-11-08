#sets in python-{}

# this data types cannot print repeated words.
a={1,"2",3,4,5,4,3}
print(a)
print(type(a))
# sete are not indexable
#print(a[-1])
#this is a empty dictionary not an empty set.
b={}
print(type(b))
# this is an empty set
c=set()
c.add(14)
c.add(4)
c.add(13)
c.add((1,2,3))
print(c)
print(type(c))

#sets method

s={1,2,3,4,5,6,7}
# it returns the length of set.
print(len(s))
#it remove the elment in the set.
(s.remove(2))
print(s)
# it removes the very first element.
print(s.pop())
print(s)
# it removes all elments in the set.
#s.clear()
# it add this set to the oringial set.
print(s.union({7,8,9}))
# it will take elements from both the set.
(s.intersection({8,9}))
print(s)