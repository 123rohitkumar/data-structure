#search duplicate in list.
def find_duplicate(numbers):
    duplicate = []
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if numbers[i] == numbers[j]:
                duplicate.append(numbers[i])


    return duplicate

numbers = [3,6,2,4,3,6,8,9]
res=find_duplicate(numbers)
print(res)





