import pandas as pd
import tabulate as tb
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter.filedialog import askopenfilename
import pandas as pd

df = pd.read_csv('CorData.csv',low_memory=False)

#dtype={"value": float},
#usecols=['country','type','value'],
#na_values =['.','??'])


df_columns = df.columns.tolist()

#Specific Columns
df_duplicates = df.duplicated(keep=False)
dupe_row = df_duplicates[df_duplicates.duplicated()]


#All Columns
df_duplicates_col = df.duplicated(keep=False,subset=['year_week', 'cases_weekly'])
dupe_row_col = df_duplicates_col[df_duplicates_col.duplicated()]

#Average_val = df.groupby('country').mean()


pd.set_option('display.max_colwidth', None) 
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 2000)
pd.set_option('display.float_format', '{:20,.2f}'.format)



print(df)
print(df_duplicates_col)
#print(Average_val)


