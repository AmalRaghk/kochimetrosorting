import pandas as pd
def group(data,q):
   data_sum = data.rename(columns={"Name": "Name"})
   data_sum["Sum"] = data[q].sum(axis=1)
   return data_sum[['Name', 'Sum']]
def heap_sort(data):
    build_heap(data)
    for i in range(len(data)-1,0,-1):
        data.iloc[0],data.iloc[i]=data.iloc[i],data.iloc[0]
        heapify(data,0,i)
    return data
def build_heap(data):
    for i in range(len(data)//2 -1,-1,-1):
        heapify(data,i,len(data))
def heapify(data,index,heap_size):
    largest=index
    left=index*2+1
    right=index*2+2
    if left<heap_size and data.iloc[left][1]>data.iloc[largest][1]:
        largest=left
    if right<heap_size and data.iloc[right][1]>data.iloc[largest][1]:
        largest=right
    if largest != index:
        data.iloc[index],data.iloc[largest]=data.iloc[largest],data.iloc[index]
        heapify(data,largest,heap_size)

data=pd.read_csv("./heapdata.csv")
q1=group(data,["Jan", "Feb", "Mar"])
q2=group(data,["Apr", "May", "Jun"])
q3=group(data,["Jul", "Aug", "Sep"])
q4=group(data,["Oct", "Nov", "Dec"])
q1_sort=heap_sort(q1)
q1_sort.to_csv('q1.csv',index=False)
q2_sort=heap_sort(q2)
q2_sort.to_csv('q2.csv',index=False)
q3_sort=heap_sort(q3)
q3_sort.to_csv('q3.csv',index=False)
q4_sort=heap_sort(q4)
q4_sort.to_csv('q4.csv',index=False)









