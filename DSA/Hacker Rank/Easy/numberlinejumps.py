
# given two positions and starting speeds. find when both of them will intersect.

# init 
x1 = 0
v1 = 2
x2 = 5 
v2 = 3

counter = 1 # independent variable of func 
flag = True # while loop

max_iteration = 100000 # 

# init functions 
y1 = (x1 + (v1*counter))
y2 = (x2 + (v2*counter))


# Function:   = x1 + v1(i)

while(flag and (y1 < max_iteration or y2<max_iteration)):
    
    y1 = (x1 + (v1*counter))
    y2 = (x2 + (v2*counter))
    counter += 1
    
    if y1 == y2:
        print("YES")
        flag = False
        
# if flag is true, it means that it reached the condition where y1 and y2 < max iteration Therefore no

if (flag):
    print("No")