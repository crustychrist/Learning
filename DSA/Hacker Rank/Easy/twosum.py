

nums =  [2, 7, 11, 15]
target = 9

# Finding the complement

def twosums(nums,target):
    nums_map = {}
    for i, num in enumerate(nums):
        complement = target - num

        if complement in nums_map:
            print ([nums_map[complement],i]) # i is your current index that is being printed
            return [nums_map[complement],i]
    
        nums_map[num] = i 
    
    return None 


twosums(nums,target)