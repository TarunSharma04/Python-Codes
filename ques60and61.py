# write a program to make a copy of the text file "this.txt".
with open("this.txt","r") as f:
  content=f.read()
with open("copy.txt","w") as f:
    f.write(content)

#ques=write a program to find out whether a file is identical and matches the content of another file.
F1="this.txt"
F2="copy.txt"
with open("this.txt")as f:
     F1=f.read()
with open("copy.txt")as f:
     F2=f.read()
if F1==F2:
  print("FILES ARE IDENTICAL")
else:
  print("files are not identical")