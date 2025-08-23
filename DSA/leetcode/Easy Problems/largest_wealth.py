# init 
accounts = [[2,8,7],[7,1,3],[1,9,5]]
sum_container = list()


# Containerizing sums
for x in accounts:
    sum(x)
    sum_container.append(sum(x))


#output
print(max(sum_container))