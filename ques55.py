# ques=the game()function in a program tells a user play the game
# and returns the  score as an integer.you need to read the file"hiscore.txt'
# which is either blank or contains the previous hi-score.you need to write
# a programs to update  the hi-sore whenever game()breaks the hi-score.


def game():
    return 167

# this is our's score.False
score = game()

# it read the value kept in hiscore.txt
with open("hiscore.txt")as f:
    hiscore = int(f.read())

if (hiscore) < score:
    with open("hiscore.txt", "w")as f:
        f.write((str(score)))
