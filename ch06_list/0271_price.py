import random

prices = [random.randint(100, 500), random.randint(50, 500), random.randint(20, 500), random.randint(10, 500), ]
cheapest = prices[0]

for i in range(1, len(prices)):

    if prices[i] < cheapest:
        cheapest = prices[i]

print("가장 싼 가격은 ", cheapest)
