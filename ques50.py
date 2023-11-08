# writ aprogram to print a star pattern using functions.
''' *****
    ****
    *** 
    **
    *   '''

def star_pattern(n):
    for i in range(n):
        print("*"*(n-i))

star_pattern(4)