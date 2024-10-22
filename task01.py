import time

coins=[50, 25, 10, 5, 2, 1]

def find_coins_greedy(amount, coins):
    result = {}
    for coin in coins:
        if amount == 0:
            break
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount -= coin * count
    return result

def find_min_coins(amount, coins):
    # Ініціалізуємо масив для зберігання мінімальної кількості монет для кожної суми
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    # Заповнюємо масив
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # Визначаємо набір монет для досягнення суми
    result = {}
    while amount > 0:
        for coin in coins:
            if amount >= coin and dp[amount] == dp[amount - coin] + 1:
                result[coin] = result.get(coin, 0) + 1
                amount -= coin
                break
    return result

def measure_time(func, *args):
    start = time.time()
    result = func(*args)
    end = time.time()
    return result, (end - start) * 1_000_000

amount_list = [113, 8922, 23941, 64999, 124857]

for amount in amount_list:
    greedy_result, greedy_time = measure_time(find_coins_greedy, amount,coins)
    dp_result, dp_time = measure_time(find_min_coins,amount,coins)

    print(f"Жадібний алгоритм:{greedy_result} \t час виконання для суми {amount}:{greedy_time:.8f} мкс")
    print(f"Динамічне програмування:{dp_result} \t час виконання для суми {amount}:{dp_time:.8f} мкс")