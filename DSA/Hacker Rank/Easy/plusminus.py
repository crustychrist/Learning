# init 
arr = [-4, 3, -9, 0, 4, 1]
positive = 0
zero = 0
negative = 0
length = len(arr)
output_arr = [0]*3

# find the ratio of zeros,positives and negative integers

for x in range(length):
        
    if arr[x] < 0:
        negative += 1
        
    if arr[x] > 0:
        positive += 1
        
    if arr[x] == 0:
        zero +=1
        
# finding ratios, positive,negative,zeros
print("{:.6f}".format(positive/length))
print("{:.6f}".format(negative/length))
print("{:.6f}".format(zero/length))

