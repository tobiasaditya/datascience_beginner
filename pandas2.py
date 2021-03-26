import pandas as pd

#Merging
food={'number':[1,2,3,4,5],
      'names':['corn','banana','pizza','sushi','fish and chip'],
      'price':[8,3,4,8,6]}

food1={'number':[1,2,3,4,5],
      'names':['apples','banana','pizza','sushi','bean'],
      'price':[2,3,4,8,6]}

table=pd.DataFrame(food)
table1=pd.DataFrame(food1)

fusion = pd.merge(table,table1)

print(fusion)

fusion1=pd.merge(table,table1, on="number")

print(fusion1)