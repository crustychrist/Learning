

# getting inputs and setting it up
word = input("PLease enter the string to be reversed: ")
char_word = list(word)
array_string = [ ]
# reverse for loop

# reverse the loop 
counter = 1 # init counter
for i in range(len(char_word),0,-1):
    array_string[counter] = i
    counter = counter + 1
    print(i)
    print(array_string)





