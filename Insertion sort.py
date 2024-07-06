def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1
  

  
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key  # Insert the key at the correct position

    print(arr)

a = [213, 5, 2, 1, 8, 7]
insertion_sort(a)



