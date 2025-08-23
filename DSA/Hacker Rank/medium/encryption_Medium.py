'''/*

An English text needs to be encrypted using the following encryption scheme.
First, the spaces are removed from the text. Let be the length of this text.
Then, characters are written into a grid, whose rows and columns have the following constraints:

Steps:
-  spaces removed from string
-  charcters written into a grid. 
- L = length of text 
- Floor and ceil of the root corresponds to ( Length * Width )
- maybe a check for rows * columns >== to L
-  
'''
import math



# Removing string spaces

str = "a string with spaces";
str = str.strip();
str =  str.replace(" ", "");
print(str)

L =len(str)
root_L = math.sqrt(L);
floor_L = math.floor(root_L); # Width
ceil_L = math.ceil(root_L); # Length 

# Creating matrix

matrix=[]
for i in range(ceil_L):                  # Creating 2D array of m*m
    matrix.append([])
    for j in range(ceil_L):
        matrix[-1].append("#")
print(matrix)


