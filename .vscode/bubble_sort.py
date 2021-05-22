def bubble_sort(array):
    n = len(array)

    for i in range(n):
        for j in range(n-i-1):
            if array[j]>array[j+1]:
                temp = array[j+1]
                array[j+1] = array[j] 
                array[j] = temp
    
    return array
res = bubble_sort([5,11,12,14,9,78])
print(res)


