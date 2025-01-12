def birthdayCakeCandles(candles):
    tallest = max(candles)

    tallest_count = 0

    for candle in candles:
        if candle == tallest:
            tallest_count += 1

    return tallest_count


if __name__ == '__main__':

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)
