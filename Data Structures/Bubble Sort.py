def BubbleSort(list):

    n=len(list)

    for i in range(n-1,0,-1):
        for j in range(i):
            if list[j]> list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]




    
    return list

list=[5,8,2,9,1,6]
print(BubbleSort(list))
