#string function

a="my name is ayush sahoo"
print(len(a))
# prints the length of the string.
print(a.endswith("hoa"))
# prints the words from which string endswith.
print(a.startswith("ayu"))
# prints the words from which string startswith.
print(a.count('a'))
# prints the count of the alphabet presents in the string.
print(a.capitalize()) 
# capitalize the first alphabet present in the string.
print(a.find("s"))
# it finds the word/alphabet in the string which occurs first and prints the index of it.
print(a.replace("name","fame"))
# it replaces the old word into new word in the string.
print(a[::-1])

# escape sequence characters
b="my\tname\"is\nayush\'sahoo\\"
print(b)
'''\n=used for new line 
\t=used for space
\'=used for single quote
\"=used for double quote
\\= used for backlash'''