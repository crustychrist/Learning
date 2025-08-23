
#Input
candies = [4,2,1,1,2]
extraCandies = 1
result = []
largest_element = candies[0]

#Find Biggest element in array
for x in candies:
    if (largest_element < x) :
        largest_element = x

print(largest_element)


for x in candies:
    if ((x + extraCandies) >= largest_element):
        result.append(True)
    else:
        result.append(False)

print(result)