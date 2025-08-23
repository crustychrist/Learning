

# init
array_2 = [[-9,-9,-9,1,1,1], [0,-9,0,4,3,2], [-9,-9,-9,1,2,3], [0,0,8,6,6,0], [0,0,0,-2,0,0], [0,0,1,2,4,0]]
max_sum = -100000

for j in range(4):
    for i in range(4):
    
        
        temp = ((array_2[j][i] + array_2[j][i+1] + array_2[j][i+2]) +  (array_2[j+1][i+1]) + (array_2[j+2][i]+array_2[j+2][i+1]+array_2[j+2][i+2]))
        
        if(temp > max_sum):
            max_sum = temp

print(max_sum)        