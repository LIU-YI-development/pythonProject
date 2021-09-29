import pandas as pd
import os

path1 = "C:\\Users\\YiLIU\\Desktop\\Pandas-Data-Science-Tasks-master\\SalesAnalysis\\Sales_Data\\Sales_April_2019.csv"
path2 = 'C:\\Users\\YiLIU\\Desktop\\Pandas-Data-Science-Tasks-master\\SalesAnalysis\\Sales_Data\\'
df = pd.read_csv(path1)

files = [file for file in os.listdir('C:\\Users\\YiLIU\\Desktop\\Pandas-Data-Science-Tasks-master\\SalesAnalysis\\Sales_Data\\')]

all_months_data = pd.DataFrame()

for file in files:
    df = pd.read_csv("C:\\Users\\YiLIU\\Desktop\\Pandas-Data-Science-Tasks-master\\SalesAnalysis\\Sales_Data\\"+file)
    all_months_data = pd.concat([all_months_data, df])

# all_months_data.to_csv(path2+"all_data.csv",index=False)
