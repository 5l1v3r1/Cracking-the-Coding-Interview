# BUGGY: Given an in nite number of quarters (25 cents), dimes (10 cents), nickels (5 cents) and pennies (1 cent), write code to calculate the number of ways of representing n cents

def howPay(cost, coins):
    if cost == 0:
        return 1

    if cost < 0:
        return 0

    res = 0
    for coin in coins:
        res += howPay(cost - coin, coins)
    return res

if __name__ == '__main__':
    print(howPay(20, [25, 10, 5]))
    # 10 10
    # 10 5 5
    # 5 5 5 5
