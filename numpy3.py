import numpy as np

var1= np.array([(1,3,5),(2,4,6)])
print(var1)
#Untuk nyatuin jadi satu array
print(var1.ravel())

#Sum array axis
print(var1.sum(axis=0)) #Totalin per masing" elemen
print(var1.sum(axis=1)) #Titakubbta per baris

#Sqrt
print(np.sqrt(var1))

#Std
print(np.std(var1))


