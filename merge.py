def merge(arr,p,q,r):
    L=[]
    R=[]
    n1=q-p+1
    n2=r-q
    for i in range(0,n1):
        L.append(arr[p+i])
    for j in range(0,n2):
        R.append(arr[q+j+1])

    L.append(1000)
    R.append(1000)
    i=0
    j=0
    for k in range(p,r+1):
        if L[i]<=R[j]:
            arr[k]=L[i]
            i=i+1
        else:
            arr[k]=R[j]
            j=j+1

def merge_sort(arr,p,r):
    if p<r:
        q=((p+r)//2)
        merge_sort(arr,p,q)
        merge_sort(arr,q+1,r)
        merge(arr,p,q,r)
    return arr
arr=[1,4,5,6,3,2]
print(merge_sort(arr,0,5))