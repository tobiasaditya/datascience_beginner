import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

person = {'finances':[1,2,3,4,5,6,7,8,7,6,5,4,3,2,1,7,4,1,8,5,2,9,6,3,9,8,7,6,5,4,3,2,1,1,9,7,3,8,2,7],
           'management':[1,2,3,4,5,6,7,8,7,6,5,4,3,2,1,7,4,1,8,5,2,9,6,3,9,8,7,6,5,4,3,2,1,1,9,7,3,8,2,7],
           'logistic':[1,2,3,4,5,6,7,8,7,6,5,4,3,2,1,7,4,1,8,5,2,9,6,3,9,8,7,6,5,4,3,2,1,1,9,7,3,8,2,7],
           'get_work':[0,0,1,0,0,1,0,0,1,1,1,1,1,1,1,0,0,0,1,0,0,1,0,0,1,1,0,1,0,0,0,0,1,1,1,0,1,0,0,1]
           }

database = pd.DataFrame(person, columns=['finances','management','logistic','get_work'])

print(database[['finances','management','logistic']])

x = database[['finances','management','logistic']]
y = database['get_work']

#30% buat tes, 70 buat training
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=0)

lr=LogisticRegression()
lr.fit(x_train,y_train)

y_predict=lr.predict(x_test)

confusion_mat = pd.crosstab(y_test,y_predict,rownames=["true"],colnames=["prediction"])

sb.heatmap(confusion_mat,annot=True)

print("Accuracy = ", metrics.accuracy_score(y_test,y_predict))
print(confusion_mat)
plt.show()

