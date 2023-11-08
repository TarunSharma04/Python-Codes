# Dictionary

dictionary = {"apple": "it is a software company",
              "google": "it is fastest growing tech company in the world",
              "facebook": "it is a social media interface",
              "instragram": "it is an another social media interface",
              "list":"[1,'ayush',34,65]",
              "tuple":"(11,23,45,56)"}
              #key     #value
print(dictionary)
#dictionary{"key":"value",}
print(dictionary["list"])
print(dictionary["tuple"])
print(dictionary["apple"])

#dicitinary methods

#It is a method which returns the list of (key,value) in tupple form.
print(dictionary.items()) 
# It is a method which returns the list of the keys present in your dictionary .
print(dictionary.keys()) 
print(dictionary.values()) 
# It is a method to update the dictionary.
#it is just a modification line.
dictionary.update({"apple":"it is a fastest growing tech company","tuple":"(12,34,60)"})
print(dictionary)
# it is the method which returns the value of specified keys.
print(dictionary.get("apple"))