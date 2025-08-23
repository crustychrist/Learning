input = [1,2,3,4,5,4,3,2,1,3,4]
types = list(dict.fromkeys(input)) # removes duplicates to get types
coll = {}

for i in types:
    value = input.count(i)
    coll[i] = value
    
# Extract the keys
print(max(zip(coll.values(), coll.keys()))) 