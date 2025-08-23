# init
arr = [[1,2,3],[4,5,6],[9,8,9]]
length = len(arr)
sum_right = 0
sum_left = 0
index_right = 0
index_left = length - 1

# Summing right diag
for j in range(length):
    sum_right += arr[j][index_right]
    index_right += 1
    
for j in range(length):
    sum_left += arr[j][index_left]
    index_left -= 1
    