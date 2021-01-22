import pandas as pd
import tabulate as tb
import matplotlib.pyplot as plt


df = pd.read_csv(
'CoronaData.csv', 
low_memory=False,
dtype={"value": float},
usecols=['country', 'type'],
na_values =['.','??']
)

#Corona.groupby('country').value.sum().plot(kind='bar')
#df.groupby('country','type').plot(kind='bar')
df.groupby('country').sum('type').plot(kind='bar')

#plt.plot(Corona['country'], Corona['population'], Corona['date'])


plt.show()

#x = Corona.country
#y = Corona.population
#plt.plot(x,y)
#plt.scatter(x, y)
#plt.show(kind=bar)

#plot(col1, col2)
#print(Corona)

