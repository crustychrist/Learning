import math
 
def encryption(s):
    n=len(s)
    m=math.ceil(math.sqrt(n))           # Dimension/side length of matrix
    matrix=[]
    for i in range(m):                  # Creating 2D array of m*m
        matrix.append([])
        for j in range(m):
            matrix[-1].append("#")
    index=0
    for i in range(m):                # Traverse row-wise and write the string in matrix
        for j in range(m):
            if index<n:
                matrix[i][j]=s[index]
            index+=1
    # Note that if the letter is "#" we don't print it
    for j in range(m):              # Traverse column-wise and print the letters
        for i in range(m):
            if matrix[i][j]!="#":
                print(matrix[i][j],end="")
        print(" ",end="")
 
s = input()
encryption(s)