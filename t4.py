def b_sort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
def mean(arr):
    return (sum(arr)/len(arr))
arr=list(map(int,input("number other then 1000").split()))
print(b_sort(arr),mean(arr))
