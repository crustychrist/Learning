# How many times does she break scores

input =  [10,5,20,20,4,5,2,25,1]
best_score = input[0]
lowest_score = input[0]
best_score_counter = 0
lowest_score_counter = 0

for i in input:
    
    if i > best_score:
        best_score = i
        best_score_counter += 1
            
    if  i < lowest_score:
        lowest_score = i
        lowest_score_counter += 1
        
        
print ("She beat her best score: " + str(best_score_counter))
print("she broke her lowest score: " + str(lowest_score_counter))
        