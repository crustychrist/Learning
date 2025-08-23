nums = [3,2,2,3] 
val = 3

def removeNumber(nums,val):
    
    #init index
    index = 0

    for x in nums: 
        if nums[index] != val:
            nums[index] = nums[index]
            index += 1
        else:
            nums.remove(x)
            index += 1  

    length = len(nums)
    print('the array is: ' + str(nums) + 'of length ' + str(length))


removeNumber(nums,val)