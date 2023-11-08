# ques= a file contains a word "donkey" mutiple times.you need to write
# aprogram which replaces this word with #### by updating
# the same file.

# ques=repat the previous program for a list of such words to be censored.
lists = ["donkey", "bhalu", "aaloo", "kutta"]

with open('3.txt', 'r') as f:
    text = f.read()

for list in lists:
    text = text.replace(list, "######")
    with open("3.txt", "w") as f:
        f.write(text)