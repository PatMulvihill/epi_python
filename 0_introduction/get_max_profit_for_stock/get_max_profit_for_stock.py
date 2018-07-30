# brute force: 0(n^2) b/c nested loops
def bf_get_max_profit_for_stock(L, H, S):
    max_profit = 0
    for i in range(len(S)):
        for j in range(len(S)):
            if j > i:
                profit = S[j] - S[i]
                if profit > max_profit:
                    max_profit = profit

    return max_profit

# linear: 0(n) b/c we iterate through S one time
def get_max_profit_for_stock(L, H, S):
    max_profit = 0
    min_buy_price = float('inf')
    for price in S:
        if price < min_buy_price:
            min_buy_price = price
        elif price - min_buy_price > max_profit:
            max_profit = price - min_buy_price

    return max_profit


L = []
H = []
S = [15, 9, 13, 12, 15, 10, 12, 15, 7, 8, 10, 8, 7, 3, 5, 9, 4, 1, 5, 9]

max_profit_brute = bf_get_max_profit_for_stock(L, H, S)
print("max_profit_brute = ", max_profit_brute)

max_profit = get_max_profit_for_stock(L, H, S)
print("max_profit_linear = ", max_profit)