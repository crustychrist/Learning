# It has to be continuous

s = "RLRRRLLRLL"
char_s = list(s)
balanced = 0 # needs to start at 1
result = 0

# Simple For LOOP
for x in range(0, len(char_s)):
    if (char_s[x] == 'R'):
        balanced = balanced + 1
        
    if (char_s[x] == 'L'):
        balanced = balanced - 1
        
    if(balanced == 0):
        result = result + 1

print(result)