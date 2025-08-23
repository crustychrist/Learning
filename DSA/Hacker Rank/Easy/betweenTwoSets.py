# Given two arrays. The eleemnts of the first array are all factors of the integer beign considered 
# Create a function that generates the factors of an integer
# Create a function that generates the multiples of an integer.
# Use your factors as the boundary condition. A factor stops only at its self.


# Init
a = [2,6]
b = [24,36]
big_container = []
small_container = []
flag = False

# Find Factors, Take biggest number as your limiter (Boundary condition)

for i in b:
    if flag:    
        big_container.append(small_container)
        small_container = []
        flag = False
        
    for y in range (1,i+1):
        if i%y == 0:
            small_container.append(y)
            flag = True 

# Adding condition:
if flag:
    big_container.append(small_container)
    flag = False

#Find multiples
max_num = max(max(big_container))


#Find multiples
#for i in range(max_num + 1):
    
sum = 0
multiple_flag = False
multiple_container = []
multiple_small_container = []

for i in a:
    sum = i  
    if multiple_flag:
        multiple_flag = False
        multiple_container.append(multiple_small_container)
        sum = 0 
        multiple_small_container = []
    
    while(sum < max_num):
        sum += i
        multiple_small_container.append(sum)
        multiple_flag = True
        
multiple_container.append(multiple_small_container)

# Find common multiple in each, doing two intersects 

intersection_1= (set.intersection(*[set(list) for list in multiple_container]))
intersection_2 = (set.intersection(*[set(list) for list in big_container]))

# typecast
intersection_1 = list(intersection_1)
intersection_2 = list(intersection_2)
final_container = []
final_container.append(intersection_1)
final_container.append(intersection_2)


final_intersection =  (set.intersection(*[set(list) for list in final_container]))
print(final_intersection)

