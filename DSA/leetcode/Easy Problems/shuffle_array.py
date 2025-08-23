#input
array = [1,2,3,4,4,3,2,1]
n = 4

# X & Y
x_list = list()
y_list = list()
result = list()

for x in range(0,n):
    x_list.append(array[x])

for y in range(n,(2*n)):
    y_list.append(array[y])


# shuffle
for x in range(0,n):
    result.append(x_list[x])
    result.append(y_list[x])

print(result)