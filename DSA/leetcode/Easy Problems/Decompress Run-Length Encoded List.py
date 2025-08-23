
#inputs: Soln not efficient 
input = [1,2,3,4]
pairs = []
pair = []
equal_counter = 0



#Creates an array of Pairs
for i in input :
    if (equal_counter == 1):
        pair.append(i)
        pairs.append(pair)
        pair = []
        equal_counter = 0
    else:
        print(i)
        pair.append(i)
        equal_counter = equal_counter + 1


solution = []
for i in range(0,len(pairs)-1):
    for j in range(0,len(pairs)-1):
        