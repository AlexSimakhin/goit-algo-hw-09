"""task.py"""
import time
from collections import defaultdict

# Номінали монет, доступні для розрахунку
coins = [50, 25, 10, 5, 2, 1]

# Жадібний алгоритм для знаходження мінімальної кількості монет
def find_coins_greedy(amount):
    result = {}  # Словник для збереження кількості кожного номіналу
    for coin in coins:
        if amount >= coin:  # Якщо поточний номінал підходить
            result[coin] = amount // coin  # Визначаємо кількість монет цього номіналу
            amount %= coin  # Оновлюємо залишок суми
    return result

# Динамічне програмування для знаходження мінімальної кількості монет
def find_min_coins(amount):
    min_coins = [0] + [float("inf")] * amount  # Масив мінімальних монет для кожної суми
    coin_count = [defaultdict(int) for _ in range(amount + 1)]  # Масив для збереження розподілу монет

    for coin in coins:
        for x in range(coin, amount + 1):
            # Якщо новий варіант кращий за попередній
            if min_coins[x - coin] + 1 < min_coins[x]:
                min_coins[x] = min_coins[x - coin] + 1  # Оновлюємо мінімальну кількість монет
                coin_count[x] = coin_count[x - coin].copy()  # Копіюємо попередній набір монет
                coin_count[x][coin] += 1  # Додаємо поточну монету

    return dict(coin_count[amount])  # Повертаємо оптимальну комбінацію монет

# Тестові суми для перевірки ефективності алгоритмів
amounts = [113, 26, 60, 73, 999, 1234]

print("Amount | Greedy Time (s) | DP Time (s)")
for amount in amounts:
    # Вимірювання часу для жадібного алгоритму
    start = time.perf_counter()
    greedy_result = find_coins_greedy(amount)
    time_greedy = time.perf_counter() - start

    # Вимірювання часу для алгоритму динамічного програмування
    start = time.perf_counter()
    dp_result = find_min_coins(amount)
    time_dp = time.perf_counter() - start

    # Виведення результатів
    print(f"{amount:>6} | {time_greedy:>14.8f} | {time_dp:>12.8f}")
    print(f"Greedy: {greedy_result}")
    print(f"DP: {dp_result}\n")
