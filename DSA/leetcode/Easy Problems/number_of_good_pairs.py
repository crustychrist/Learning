#Given an array of integers nums.
#A pair (i,j) is called good if nums[i] == nums[j] and i < j.
#Return the number of good pairs.

# Initialisation
input_array = [1,2,3]
combinations = []
index = 1 # start array at index 1

# Algo, Simply a nested for loop checking the condition.Not the most efficient.
result = 0
for i in range(0,len(input_array)): 
    for j in range(index,len(input_array)):
        if ( (i < j) and (input_array[i] == input_array[j])):
            result = result + 1

    index = index + 1

# Alternative Soln: Create dictionary with Element as Key and Frequency as Value and put it into a
# Binomial form. ( N!/ r!(N-R)!) 


