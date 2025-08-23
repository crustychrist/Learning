# Jewels and Stones
J = "z"
S = "ZZ"

# convert string to list
J_arr = list(J)
S_arr = list(S)

counter = 0
for x in J_arr:
    for i in S_arr:
        if x == i:
            counter = counter + 1


print(counter)