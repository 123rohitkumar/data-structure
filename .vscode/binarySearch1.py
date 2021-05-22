# iterative approch
# note-->array should be shorted manner then only binary seach is possible. 
# arr = [ 2, 3, 4, 10, 40,50 ] 
#x = 10
def binary_search(arr,x):
    high = len(arr)
    low = 0

    while high>=low:

        mid = (high+low)//2

        if arr[mid]==x:
            return mid

        #if element value less then mid-index-value
        #search left side
        elif x < arr[mid]:
            high = mid-1

        else:
            low = mid+1

    # If we reach here, then the element was not present 
    return -1

arr = [ 2, 3, 4, 10, 40,50,60,75] 
x = 2

result = binary_search(arr,x)       
if result != -1: 
    print("Element is present at index", str(result)) 
else: 
    print("Element is not present in array") 



