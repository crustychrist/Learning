
# Init
arr = []
N = 3
lastAnswer = 0
lastAnswer_arr = []

# Creating 2D array
for i in range(N):
    arr.append([])
    

# Queries string
queries = ['105','117','103','210','211']
queries_temp = []


# performing operations
# 2x loop = BIG O^2
for i in queries:
     queries_temp = list(i) # break it up
     
     for x in range(len(queries_temp)):
         queries_temp[x] = int(queries_temp[x])
    
     #Query 1:idx = ((X ^ last answer) % 2 ) 
     if (queries_temp[0] == 1):
         idx = ((queries_temp[1] ^ lastAnswer)%N)
         arr[idx].append(queries_temp[2])
         
     elif(queries_temp[0] == 2):
         idx = ((queries_temp[1] ^ lastAnswer)%N)
         lastAnswer = arr[idx][queries_temp[2]%len(arr[idx])]
         lastAnswer_arr.append(lastAnswer)


print(lastAnswer_arr)

