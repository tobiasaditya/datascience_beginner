import pandas as pd

food={'number':[1,2,3,4,5],
      'names':['corn','banana','pizza','sushi','fish and chip'],
      'price':[8,3,4,8,6]}

food1={'colors':["red","yellow","meaty","green","golden"],
      'weight':[100,200,150,175,225],
      'quantity':[1,2,1,3,4]}

table1 = pd.DataFrame(food)
table2 = pd.DataFrame(food1)

fusion = table1.join(table2)

print(fusion)