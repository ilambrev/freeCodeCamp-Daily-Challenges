def burn_candles(candles, leftovers_needed):
    leftovers = 0
    total = 0

    while candles > 0:
        total += candles
        leftovers += candles
        candles = int(leftovers / leftovers_needed)
        leftovers = leftovers % leftovers_needed

    return total

# print(burn_candles(7, 2))
# print(burn_candles(10, 5))
# print(burn_candles(20, 3))
# print(burn_candles(17, 4))
# print(burn_candles(2345, 3))