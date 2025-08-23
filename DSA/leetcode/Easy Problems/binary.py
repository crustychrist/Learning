
from turtle import end_fill


input = [1,2,3,4,5] 
target = 4

# to solve this, must use log(n)

def binarySearch(input,target):
    
    # Init
    length = len(input)
    high = length - 1

    low = 0
    index = int(((high-low)/2))

# Binary Search, proper way is recursive
    while(int(input[index]) != target):

        if (( target > input[index])): #move right 
            low = index
            index = abs(int((((high+low)/2))))
    
        elif (( target < input[index])):
            high = index
            index = abs(int((((high+low)/2))))


    return index 


index = binarySearch(input,target)
print('The index of ' + str(target) + ' is '+ str(index))