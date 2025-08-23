import math
''' Soln
    cases:
    1) If result under 40 = fail
    2) if the grade is over 40, and the difference between the next multiple of 5 is less than 3. round up to the closest multiple of 5 
    3) func  for rounding = multiple * round (number / multiple )
'''

# Sample Input and inits
grades = [4,73,67,38,33]
rounded_grades = []
multiple = 5


for i in grades[1:]:
    
    rounded_number = multiple * (round(math.ceil(i/multiple))) 
    
    if rounded_number < 40:
        rounded_grades.append(i)
        pass
    
    elif rounded_number >= 40:
        
        if (rounded_number - i) < 3:
            rounded_grades.append(rounded_number)
        
        else:
            rounded_grades.append(i) 

print(rounded_grades)
        
    
    