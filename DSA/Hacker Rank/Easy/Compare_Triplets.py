
# Init 
input_alice = [17,28,30]
input_bob = [99,16,8]
alice = 0
bob = 0

# comparative 
for idx, x in enumerate(input_alice):

    if (input_alice[idx] > input_bob[idx]):
        alice += 1
    elif(input_bob[idx] > input_alice[idx]):
        bob += 1
    else:
        pass     

print("Bob points: " +str(bob))
print("alice points:" + str(alice))

if ( alice > bob):
    print ('alice has more points')

if (bob > alice):
    print('bob has more points ')