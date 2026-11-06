# Solutions for 03_lists.py

# 1
cities = ["Dallas", "Paris", "Lagos", "Tokyo", "Hurst"]
print(cities[0], cities[-1], cities[1:4])

# 2
cities.append("Kinshasa")
cities.insert(0, "Lubumbashi")
print(cities)

# 3
cities.remove("Paris")
popped = cities.pop()
print("popped:", popped, cities)

# 4
prices = [12.5, 3.0, 47.25, 8.75]
print(sum(prices), min(prices), max(prices))
print(round(sum(prices) / len(prices), 2))
print(sorted(prices, reverse=True))

# 5
def reverse_list(items):
    return items[::-1]

nums = [1, 2, 3]
print(reverse_list(nums), nums)

# 6
def add_unique(items, value):
    if value not in items:
        items.append(value)
    return items

print(add_unique(["a", "b"], "b"), add_unique(["a", "b"], "c"))

# 7
print([p for p in prices if p > 10])

# PROJECT STEP 3
history = [500, -120, 75.5, -40, 1200, -300]
deposits = [t for t in history if t > 0]
withdrawals = [t for t in history if t < 0]
print("deposits:", deposits)
print("withdrawals:", withdrawals)
print("total in:", sum(deposits), "total out:", sum(withdrawals), "balance:", sum(history))
print("last 3, newest first:", history[-3:][::-1])
