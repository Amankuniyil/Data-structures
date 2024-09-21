def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        minpos=i

        for j in range(i+1,n):
            if arr[j]<arr[minpos]:
                minpos=j
        
        arr[i],arr[minpos]=arr[minpos],arr[i]

    
    print(arr)

a=[4,6,9,1,2,3]

selection_sort(a)