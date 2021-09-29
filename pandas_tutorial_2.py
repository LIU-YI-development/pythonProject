import pandas as pd
import numpy as np

df = pd.read_excel('C:\\Users\\YiLIU\\Desktop\\Water quality.xlsx')

# a = df[['Ca','Mn']]

a = df.iloc[0,:]
print(a)

# a= df.loc[2:,['HCO3','Mg']]

# a = df.loc[df['Ca']>88]
# a = df.loc[df['Ca']>88]

# a = df.loc[(df["Ca"]>88) & (df['Ca']<=120)]

# a = df.loc[df.UNION == 'Aliabad']

# a = df[df.UNION.str.contains('Aliabad')]

# a = df[df.UNION.str.contains('^A')]

# a = df.shape

# a = len(df)

# a = df.shape[0]

# a = df.describe()

# a = df.info()

# a = df.Ca.dtype

# a = df.UNION.unique()

# a = df.UNION.unique().shape[0]

# a = df.Ca.unique().shape[0]

# df = df.rename(columns = {'UNION':'Location'})

# a = df.max()

# a = df.min()

# a = df.mean()

# a = df.Mn.max()

# a = df.Mn.agg(['mean','std'])

# a = df.skew()

# a = df.kurtosis()

# df.drop(['LAT_DEG', 'LONG_DEG'], axis=1, inplace=True)

# a = df.groupby('UNION').mean()

# a = df.groupby('UNION').mean().plot( kind = 'bar')

# a = df.groupby(['UNION','WELL_DEPTH']).mean()

# df = pd.DataFrame({'A': [1, 1, 2, 1, 2],
#                    'B': [np.nan, 2, 3, 4, 5],
#                    'C': [1, 2, 1, 1, 2]}, columns=['A', 'B', 'C'])
#
# print(df)
# print('-----------')
# print(df.groupby('A').mean())


