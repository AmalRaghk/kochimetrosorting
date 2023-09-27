#kochi metro card users fequent tranvelers list
import pandas as pd
data=pd.read_csv("./data.csv") #dataframe
def insertion_sort(data):
    for j in range(1,len(data)):
        key=data.iloc[j][3]
        keyv=data.iloc[j]
        i=j-1
        while i>=0 and data.iloc[i][3]>key:
            data.iloc[i+1]=data.iloc[i]
            i-=1
        data.iloc[i+1]=keyv
    return data

print(insertion_sort(data))
data.to_csv('output.csv',index=False)
    