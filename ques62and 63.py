#write a program to wipe out the content of a file using python.
# module used to remove python file
file="5.txt"
with open(file,"w")as f:
    f.write("")

#write aprogram to rename a file to renamed_by_python.txt.
import os

oldname="6.txt"
newname="renamed_by_python.txt"
with open(oldname)as f:
    content=f.read()
with open(newname,"w")as f:
    f.write(content)
os.remove(oldname)