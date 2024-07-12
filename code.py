import matplotlib.pyplot as plt 
import pandas as pd

file = pd.read_csv("C:/Users/Ahtisham Shami/Downloads/titanic/train.csv")

a = file.head(10)

age = a['Age']
glu = a['Glucose']

i = True
while i == True:

    def glucose():
        plt.plot(age, glu, marker='o', linestyle='-', color='b')
        plt.title('')
        plt.xlabel('age')
        plt.ylabel('glucose level')
        plt.grid(true)
        plt.show()
        return glucose

print(glucose())
