# Import pandas package
import pandas as pd
	
# Define a dictionary containing employee data
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj', 'Geeku'],
		'Age':[27, 24, 22, 32, 15],
		'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj', 'Noida'],
		'Qualification':['Msc', 'MA', 'MCA', 'Phd', '10th'] }

# Convert the dictionary into DataFrame
#df = pd.DataFrame(data)

#print(df)

#data2 = {'Name': ['Akki','Sharma','Tarun'],
 #        'Class': ['AI', 'DS', 'CS'],
  #       'Roll': ['1', '2', '3']}

#lf = pd.DataFrame(data2)
#print(lf)

#Makes own index without removing Default index

index = {'a', 'b', 'c', 'd', 'e'}
#index = input("Enter Index:")

a = pd.DataFrame(data,index)

a.reset_index(inplace=True)
#a.reset_index(Age,inplace=True)
#a.head(2)
#a.tail(2)
print(a)

