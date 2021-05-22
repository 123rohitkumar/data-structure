#recursive approch.

#note-->array should be shorted manner then only binary seach is possible. 
#arr = [ 2, 3, 4, 10, 40 ] 
#x = 10
#in every one time execuion low high and mid is changing

def binay_search(arr,low,high,x):

    if high >= low:

        mid = (high+low)//2

        #if element is present in the middle itself:
        if arr[mid] == x:
            return mid

        #if element is smaller then mid-index-value
        #search in the left subarray.
        elif x < arr[mid]:
            return binay_search(arr,low,mid-1,x)
 
        #else element only in right subarray.
        else:
            return binay_search(arr,mid+1,high,x)



    else:
        # Element is not present in the array 
        return -1

arr = [ 2, 3, 4, 10, 40,50,67,78,89,789 ] 
x=78

result = binay_search(arr,0,len(arr),x)

if result != -1:
    print("element present at index,",str(result))

else:
    print("Element is not present in array") 

