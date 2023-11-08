# lists
a=["ayush","abhishek",345]
print(a)
print(type(a))

#list indexing
l1=[7,9,"ayush"]
print(l1[0])
print(l1[1])
print(l1[2])
# print(li[3])-- this is an error
print(l1[0:2])

#various types of list methods
l2=[12,24,576,6,89,9,4,3,1]
l2.sort() #it sorts the list.
print(l2)
l2.reverse() # it reverse the list. 
print(l2)
l2.append(7) # it add any number which you gave in the list.
print(l2)
l2.insert(3,24) #it will insert insert 24 at index 3 in the List.
print(l2)
l2.pop(5)#it will delete the elment at index 2. 
print(l2)
l2.remove(24)# it will remove the given item in the list which occur first.
print(l2)