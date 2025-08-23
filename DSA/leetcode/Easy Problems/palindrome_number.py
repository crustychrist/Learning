# given a number return True if its a palindrome
# palindrome 

number = 555

#reverse number
number_rev = list(str(number))
number_cont = list()
test_list = [int(i) for i in number_rev]
counter = 0
flag = False
     
     
for x in range((len(number_rev)-1),-1,-1):
    number_cont.append(number_rev[x])


for idx, x in enumerate(number_cont):
    if (test_list[idx] == int(number_cont[idx])):
        counter += 1

    if counter == len(number_cont):
        flag = True


if(flag):
    print('The number is a palindrom')
else: 
    print('The number is not a palindrom')
