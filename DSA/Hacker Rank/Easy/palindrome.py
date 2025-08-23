class Solution(object):
    def isPalindrome(self, x):
      
        #init 
        reversed_num = 0 
        copy_x = x # need x as reference 

        while copy_x > 0:
            last_digit = copy_x % 10
            reversed_num = (reversed_num * 10) + last_digit
            copy_x = copy_x // 10

        if reversed_num == x:
            return True

        else:
            return False 