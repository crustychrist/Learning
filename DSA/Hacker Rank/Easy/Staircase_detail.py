# given n, draw a staircase
n = 4

print('1'*5)

for i in range(1, n + 1):
    print(' ' * (n - i) + '#' * i)