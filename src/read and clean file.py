import pandas as pd
import glob
import os

path = os.getcwd()
path = path.replace("src", "data")
input_files = glob.glob(path + '\*.csv')

df_list = []
for file in input_files:
    file_df = pd.read_csv(file)
    file_df = file_df.iloc[:,:-3]
    file_df.dropna(inplace=True)
    df_list.append(file_df)

