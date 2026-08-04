def insert_price(prices, p):
    prices.append(p)
    i = len(prices) - 2
    while i >= 0 and prices[i] > p:
        prices[i + 1] = prices[i]
        i -= 1
    prices[i + 1] = p
    return prices

prices = []
for p in [102.5, 98.3, 105.1, 100.0, 97.8]:
    insert_price(prices, p)
print(prices)