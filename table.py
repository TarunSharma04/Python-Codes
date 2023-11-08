from prettytable  import PrettyTable as PT

myTable = PT(['Name','Age','Branch','Ocupation'])

myTable.add_row(['Tarun','21','AI','Engineer'])
myTable.add_row(['Akki','20','DS','Doctor'])
myTable.add_row(['Sharma','19','AI','Software Engineer'])
myTable.add_row(['Manisha','45','Home','Housewife'])

print(myTable)

# from prettytable import PrettyTable as PT
Student_table = PT(['Name','Branch','Roll No.','Mobile No.','D.O.B'])
# Student_table = PrettyTable(['Name','Branch','Roll No.','Mobile No.','D.O.B'])
# Student_table.add_column(['D.O.B'])
Student_table.add_row(['Tarun','AI','01','9992592860','10/04/2001'])
Student_table.add_row(['Arun','DS','02','9992551241','03/01/2003'])
Student_table.add_row(['Mukesh','AI','03','9416856596','18/10/1976'])
Student_table.add_row(['Chand Ram','DS','04','9466832895','14/04/1955'])
Student_table.add_row(['Ritish','CSE','05','8398838362','22/01/2006'])
Student_table.add_row(['Sandeep','DS','06','8930060028','13/12/2001'])
Student_table.add_row(['Manisha','AI','07','9416856596','01/07/1978'])

print(Student_table)

