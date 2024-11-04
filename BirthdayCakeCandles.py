def BirthdayCakeCandles(candles):
    return candles.count(max(candles))

n=int(input("Enter number of candles: "))
candles=[]
for i in range(n):
    height=int(input("Enter height of candle: "))
    candles.append(height)
print("Number of candles with max height is: ",BirthdayCakeCandles(candles))