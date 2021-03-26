import pandas as pd

employees={'number':[1,2,3,4,5],
           'name':['abby',"jeremy","toby","fransisca","lentarct"],
           "hourly salary":[15,25,32,45,40]}

table1=pd.DataFrame(employees)

print(table1)

#Ambil 3 baris pertama dari atas
print(table1.head(3))

#Ambil 3 baris dari akhir
print(table1.tail(3))


