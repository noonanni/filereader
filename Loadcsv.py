import pandas as pd
import tabulate as tb
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter.filedialog import askopenfilename
import pandas as pd


def import_csv_data():
    global v
    csv_file_path = askopenfilename()
    print(csv_file_path)
    v.set(csv_file_path)
    df = pd.read_csv(csv_file_path, 
low_memory=False,
dtype={"value": float},
usecols=['country','type','value'],
na_values =['.','??']
)

#def Summary():
 #   global v
  #  df_columns = df.columns.tolist()
   # print(df_columns)

root = tk.Tk()
tk.Label(root, text='File Path').grid(row=0, column=0)
v = tk.StringVar()
entry = tk.Entry(root, textvariable=v).grid(row=0, column=1)
tk.Button(root, text='Browse Data Set',command=import_csv_data).grid(row=1, column=0)
tk.Button(root, text='Enter',command=root.quit).grid(row=1, column=1)
root.mainloop()

df_columns = df.columns.tolist()
print(df_columns)



#countries = ['Ireland','Scotland', 'France', 'Brazil']
#Corona.groupby('country').value.sum().plot(kind='bar')
#df.groupby('country','type').plot(kind='bar')
#df.groupby('country').type.sum().plot(kind='bar')
#idx = df.groupby(['country'])['value'].transform(max) == df['value']
#max_value = value. max() get max value from "col2"
#plt.plot(Corona['country'], Corona['population'], Corona['date'])
#grouped = df.groupby(['country','type']).sum()
#df.plot(x ='country', kind = 'line')
#newdf('country').plot(kind="bar")

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

