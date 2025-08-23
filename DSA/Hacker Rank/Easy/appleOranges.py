
# init
s,t = [7,11] # distance of the house
a,b = [5,15] # distance of apple and og
m,n = [3,2] # number of apple and oranges that fell
apple_d = [-2,2,1] # apples and distance that fell
orange_d = [5,-6] # organes and distances that fell

# global distances and fruit counter
global_apple_distance = []
global_orange_distance = []
fruit_counter = []
apple_counter = 0
orange_counter = 0



# Calculate the distances of the fallen fruit
for i in apple_d:
    global_apple_distance.append(a+i)

for i in orange_d:
    global_orange_distance.append(b+i)
    

# verify if fruit falls on house
# for apples
for i in global_apple_distance:
    if(s <= i <=t):
        apple_counter += 1
        
# for oranges 
for i in global_orange_distance:
    if(s <= i <=t):
        orange_counter += 1
        
        

fruit_counter.append(apple_counter)   
fruit_counter.append(orange_counter)   

print(fruit_counter)
