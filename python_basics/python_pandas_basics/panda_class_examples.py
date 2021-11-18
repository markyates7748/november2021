import numpy as np
import pandas as pd
from numpy.random import randn

labels = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a':10,'b':20,'c':30}

pd.Series(data = my_data)

alpha = pd.Series(data = my_data, index=labels)
print(alpha)

beta = pd.Series(d)
print(beta)

print(pd.Series([1,2,3,4],['USA','Germany','Russia','Japan']))

print(alpha + beta)

df = pd.DataFrame(randn(5,4),['a','b','c','d','e'],['z','y','x','w'])
print(df)

print(df['w'])

print(type(df['w']))

print(df[['w','z']])

df['new'] = df['w']+df['y']
print(df)

print(df.drop('new',axis=1))

print(df.drop('e'))

print(df.shape)

print(df.loc['a'])

print(df.iloc[1])

print(df.drop('new',axis=1,inplace=True))

booldf = df > 0
print(booldf)

print(df[booldf])

print(df['w']>0)

print(df[df['w']>0])

#df[(df['w']>0) and (df['y']>1)]

outside = ['g1','g1','g1','g2','g2','g2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
print(hier_index)
df = pd.DataFrame(randn(6,2),hier_index,['a','b'])
print(df)
print(df.loc['g1'].loc[1])
#print(df.index.names['groups','nums'])
print(df.loc['g1'].loc[1]['b'])
print(df.xs('g1'))
#print(df.xs(1,level='nums'))

df = {'a':[1,2,np.nan],'b':[5,np.nan,np.nan],'c':[1,2,3]}
df = pd.DataFrame(df)
print(df)

print(df.dropna())

print(df.dropna(1))

print(df.fillna(value='FILL'))

data = {'Company':['goog','goog','msft','msft','fb','fb'],
        'Person':['sam','charlie','amy','vanessa','carl','sarah'],
        'Sales':[200,120,340,124,243,350]}
df = pd.DataFrame(data)
print(df)
byComp = df.groupby('Company')
print(byComp.mean())