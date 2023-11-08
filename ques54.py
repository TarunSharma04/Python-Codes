# write a program to read the text from a given file
# poems.txt and find out whether it contains the word 'twinkle'. 

with open("poems.txt","r") as f:
    t=f.read()
if 'twinkle' in t:
    print("twinkle is present")
else:
    print("twinkle is not present")