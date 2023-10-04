import pandas as pd
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
    if left<heap_size and data.iloc[left][3]>data.iloc[largest][3]:
        largest=left
    if right<heap_size and data.iloc[right][3]>data.iloc[largest][3]:
        largest=right
    if largest != index:
        data.iloc[index],data.iloc[largest]=data.iloc[largest],data.iloc[index]
        heapify(data,largest,heap_size)
data=pd.read_csv("./data.csv")
out=heap_sort(data)
out.to_csv('heapout.csv',index=False)
grouped_data = data.groupby('quarter')
q1=grouped_data.get_group(1)
q2=grouped_data.get_group(2)
q3=grouped_data.get_group(3)
q4=grouped_data.get_group(4)
q1_sort=heap_sort(q1)
q2_sort=heap_sort(q2)
q3_sort=heap_sort(q3)
q4_sort=heap_sort(q4)
q1_sort.to_csv('q1.csv',index=False)
q2_sort.to_csv('q2.csv',index=False)
q3_sort.to_csv('q3.csv',index=False)
q4_sort.to_csv('q4.csv',index=False)

