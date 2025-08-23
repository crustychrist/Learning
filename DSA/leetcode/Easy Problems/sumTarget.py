nums = [2,7,11,15]
target = 9 



def get_key(val,dict):
    for key, value in dict.items():
         if val == value:
             return str(key)


def findTarget(nums,target):
    dict = {}
    index = 0  
    for x in nums:
        difference = target - nums[index]
        
        if (difference in dict.values()):
            value1 = str(index)
            value2 = get_key(difference,dict)
            print('indexes are '+'['+ value1 + ',' + value2 + ']')
            index += 1
        else:
            dict[index] = nums[index]
            index += 1


findTarget(nums,target)