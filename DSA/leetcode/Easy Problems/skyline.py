import numpy


#RM 1 
grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
container = list()

# Station 1
#finding max sums for left and right rule
for x in grid:
    container.append(max(x))

# RM 2
container_transpose = list()

#Station 2


#Getting the transpose