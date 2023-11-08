# ques=write a program to mi9ne a log file and find out whether it contains 'python'.
# ques= write a program to find out the line where the python is present.
content=True
i=1
with open('log.txt') as f:
    while(content):
          content = f.readline()
    if 'python' in content:
        print(content)
        print("yes python is present in line",i)
        print(i)
        i=+1
#    else:
#        print('no python is not present')