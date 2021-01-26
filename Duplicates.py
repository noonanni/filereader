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

df_duplicates_specific = df.duplicated(subset=['year_week', 'cases_weekly'])


print(df_duplicates)



