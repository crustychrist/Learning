

# getting the number of available spots and rankss

spots = int(input("Please enter the number of available spots: "))
ranks = input("Please enter the ranks seperated by a space: ").split(" ")
ranks = list(map(int, ranks)) # typecast list of strings to int.

# Base condition


#sorting the ranks
ranks = sorted(ranks)

# Algo
first = ranks[0]
last = ranks[len(ranks)-1]

#creating a new list
new_list = list()
for i in range(first,last):
    new_list.append(i)

new_list.append(last)# accounting for out bounds condition

#getting spots up till first


# algo to find difference
list_difference = list()
for item in new_list:
    if item not in ranks:
        list_difference.append(item)

print(len(list_difference)- first + 2 + spots) 

#NB: Need to revisit it