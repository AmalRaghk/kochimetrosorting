import pandas as pd
def heap_sort(data,k):
    build_heap(data,k)
    for i in range(len(data)-1,0,-1):
        data.iloc[0],data.iloc[i]=data.iloc[i],data.iloc[0]
        heapify(data,0,i,k)
    return data
def build_heap(data,k):
    for i in range(len(data)//2 -1,-1,-1):
        heapify(data,i,len(data),k)
def heapify(data,index,heap_size,k):
    largest=index
    left=index*2+1
    right=index*2+2
    if left<heap_size and data.iloc[left][k]>data.iloc[largest][k]:
        largest=left
    if right<heap_size and data.iloc[right][k]>data.iloc[largest][k]:
        largest=right
    if largest != index:
        data.iloc[index],data.iloc[largest]=data.iloc[largest],data.iloc[index]
        heapify(data,largest,heap_size,k)
data=pd.read_csv("./heapdata.csv")
q1=heap_sort(data,3)
q1.to_csv('q1.csv',index=False)
q2=heap_sort(data,4)
q2.to_csv('q2.csv',index=False)
q3=heap_sort(data,5)
q3.to_csv('q3.csv',index=False)
q4=heap_sort(data,6)
q4.to_csv('q4.csv',index=False)





