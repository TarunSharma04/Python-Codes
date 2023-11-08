# write a python program to remove a given word from the list and strip it at the same time.

def process(l,word):
    word=word.strip()
    l.remove(word)
    return l

l1=["ayush","shubham","aakash","vikas","jitender"]
l1=(process(l1,"ayush"))
print(l1)