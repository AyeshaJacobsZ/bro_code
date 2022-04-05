import pandas as pd
import glob
import os

path = 'C:/Users/bronwen.barratt/Desktop/Hackathon/Hackathon_repo/bro_code/data'
#os.getcwd()
input_files = glob.glob(path + '\*.csv')

for file in input_files:
    file_df = pd.read_csv(file)
    file_df = file_df.iloc[:,:-3]
    file_df.dropna(inplace=True)

