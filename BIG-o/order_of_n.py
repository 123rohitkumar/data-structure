#time taking to execute a program is 
#equally propotinal to the number of computation is doing.

# size(arr)->100-->0.22 millisecond
# size(arr)->1000-->2.45 millisecond

#time = a*n + b  -->b is constent(intecept-->where it is cutting y axis)
#keep the fastest growing term
# time = a*n
#drop the constent
#time = n-->time complexity of this program is order of n.

#if the size is 2 million it will do 2 million repetation hence the time will
#linearly grow with the repetation means no of size of array.
#===============================================================================
# def Square_no(numbers):
#     squared_numbers=[]

#     for i in numbers:
#         squared_numbers.append(i*i)
#     return squared_numbers

# numbers = [2,3,4,5]
# result = Square_no(numbers)
# print(result)

#==============================================================
#bio-o notation is use when we want to measure the space and time 
#complexity of program as input of a fuction or array size grows
#the time of execution grows linearly.


def sum_of_array(given_array):
    total = 0
    for i in given_array:
        total +=i
    return total


given_array = [1,2,3,4,5,6]
result=sum_of_array(given_array)
print(result)

