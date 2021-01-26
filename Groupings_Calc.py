import tabulate as tb
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter.filedialog import askopenfilename
import pandas as pd

df = pd.read_csv('CorData.csv',low_memory=False, usecols=['date','country','deaths_weekly'])
#na_values =['.','??'])
#dtype={"value": float},

#DUPLICATES
#Specific Columns
df_duplicates = df.duplicated(keep=False)
dupe_row = df_duplicates[df_duplicates.duplicated()]

#All Columns
df_duplicates_col = df.duplicated(keep=False,subset=['date', 'deaths_weekly'])
dupe_row_col = df_duplicates_col[df_duplicates_col.duplicated()]

#Calculating using groupings
Average_val = df.groupby('date').mean()

#Display options of dataframe
pd.set_option('display.max_colwidth', None) 
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 2000)
pd.set_option('display.float_format', '{:20,.2f}'.format)


#Print output
#print(df)
#print(df_duplicates_col)
print(Average_val)
#plt.plot(Average_val)
#plt.show(1,2)


Average_val.plot()
plt.show()




