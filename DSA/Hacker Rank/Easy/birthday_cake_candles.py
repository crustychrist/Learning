
arr = [4,4,1,3]
tallest_candle = 0 
num_of_tallest_candles = 0

for i in range (len(arr)):
    if (arr[i] > tallest_candle):
        tallest_candle = arr[i]

for i in range(len(arr)):
    if (tallest_candle == arr[i]):
        num_of_tallest_candles += 1

print(num_of_tallest_candles)
