import pandas as pd
import glob
import os

path = 'C:/Users/bronwen.barratt/Desktop/Hackathon/Hackathon_repo/bro_code/data'
#Ayesha pls help: os.getcwd() does not work since data is not in the src folder so idk what to do
input_files = glob.glob(path + '\*.csv')

df_list = []
for file in input_files:
    file_df = pd.read_csv(file)
    file_df = file_df.iloc[:,:-3]
    file_df.dropna(inplace=True)
    df_list.append(file_df)

