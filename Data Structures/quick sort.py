def quick_sort(arr):
    if len(arr) <=1:
        return arr
    
    else:
        pivot=arr[len(arr)//2]
        left=[x for x in arr if x < pivot]
        middle=[x for x in arr if x == pivot]
        right=[x for x in arr if x > pivot]

        return quick_sort(left) +middle + quick_sort(right)
    
a=[5,6,8,3,4,1,2]

sorted= quick_sort(a)

print(sorted)