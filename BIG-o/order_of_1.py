# size(arr)->100-->0.22 millisecond
# size(arr)->1000-->0.23 millisecond 
#as size of input growing 
#but time is almost constant.

#time = a*n + b  -->b is constent(intecept-->where it is cutting y axis)
#keep the fastest growing term
# time = a*n
#drop the constent and n= 1 because size constant
#time = order(1)-->as the size incresing time for execution is almost same.
#===================================================
#search element in array by using an index ex of order of 1....

def search_ele(item):
    print(item[0])
    print(item[5])
    
item = [1,2,3,4,5,6,7]
search_ele(item) 

#this will take the same time to seach the element in list.
#so time is constant for any index