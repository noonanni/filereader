import pandas as pd
import tabulate as tb
import matplotlib.pyplot as plt


countries = ['Ireland','Scotland', 'France', 'Brazil']

df = pd.read_csv(
'CoronaData.csv', 
low_memory=False,
dtype={"value": float},
usecols=['country','type','value'],
na_values =['.','??']
)

#Corona.groupby('country').value.sum().plot(kind='bar')
#df.groupby('country','type').plot(kind='bar')
#df.groupby('country').type.sum().plot(kind='bar')
#idx = df.groupby(['country'])['value'].transform(max) == df['value']
#max_value = value. max() get max value from "col2"
#plt.plot(Corona['country'], Corona['population'], Corona['date'])
grouped = df.groupby(['country','type']).sum()



#df.plot(x ='country', kind = 'line')

#newdf('country').plot(kind="bar")


print(grouped)
grouped.to_csv("groupedtest.csv")  




#pnewdf.plot.hist();
#pplt.show()

#print(newdf)
#x = Corona.country
#y = Corona.population
#plt.plot(x,y)
#plt.scatter(x, y)
#plt.show(kind=bar)

#plot(col1, col2)
#print(Corona)

