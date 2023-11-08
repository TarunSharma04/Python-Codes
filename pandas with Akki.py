import pandas as pd

a = pd.read_csv("D:\\Tarun Sharma\\Documents\\Book1.csv")

print(a)

b = a['Marks'].max()
print(b)

c = a['Marks'].min()
print(c)

d = a['Marks'].abs()
print(d)

e = a['Marks'].sum()
print(e)

f = a['Marks'].mean()
print(f)

g = a['Marks'].count()
print(g)

