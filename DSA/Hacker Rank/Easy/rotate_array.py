

# init
arr = [1,2,3,4,5]
modulo = len(arr)
arr_result = [0]*len(arr)
d = 4

for i in range(len(arr)):
    index = (i-d)%modulo
    arr_result[index] = arr[i]
    
print(arr_result)
