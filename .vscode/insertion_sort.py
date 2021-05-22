arr = [80,70,60,50,43]


def insertion_sort(arr):
    for i in range(1,len(arr)):
        item = arr[i]
        j = i-1

        while j>=0 and arr[j] > item:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = item



if __name__ == '__main__':
    arr = [80,70,60,50,43]
    result = insertion_sort(arr)
    print(arr)













