# hamster squats, ref.424A


#Getting inputs
input_minutes = input("Please enter the minimum number of minutes: ")
input_position = input("Please enter the squatting positions")
positions= list(input_position)
outputlist = list()


# Number of minutes is given the amount of moves needed to have n/2 exercises: up or down.

small_x = 0 #init counters
big_X =  0

# find number of small x and big x
for x in positions:
    if (x == 'X'):
        big_X += 1

    elif(x =='x'):
        small_x += 1

# Base condition if it needs balancing
counter = 0
if (small_x == big_X):
    print('0 Mins')
    print(positions)


# condition loop to see that if small_X is less, find the difference so it can balance out
if (small_x < big_X):
    difference  = big_X - small_x
    for i in range((small_x + difference)-1):
        outputlist.append('x')
    for i in range(big_X-1):
        outputlist.append('X')

if (small_x > big_X):
    difference  = small_x - big_X 
    for i in range((big_X + difference)-1):
        outputlist.append('X')
    for i in range(small_x-1):
        outputlist.append('x')

print(outputlist)

# for the minutes, this is a trick, most if not all need 1 minute to balance.
