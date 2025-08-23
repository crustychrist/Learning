
# using insertion sort to arrange the array
# using indexes to parse what is needed
arr = [1,3,5,7,9]

#init
max_sum = 0
min_sum = 0
    
# sorting the array 
for i in range(1,len(arr)):
    j = i
    while (arr[j-1] > arr[j] and j > 0):
        arr[j-1], arr[j] = arr[j],arr[j-1]
        j-=1

    #slicing the array for min max
max_array = arr[1:5]
min_array = arr[0:4]

# calculating sums

max_sum = sum(max_array)
min_sum = sum(min_array)

print(str(max_sum) + " " + str(min_sum))
