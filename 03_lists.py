# 03: Lists (JS arrays)
# Run: python3 03_lists.py

# ======================= EXAMPLES =======================
nums = [10, 20, 30, 40, 50]
print(nums[0], nums[-1], len(nums), 30 in nums)

# ---- Slicing: same rules as strings ----
print(nums[1:4])      # [20, 30, 40]
print(nums[:2])       # [10, 20]
print(nums[-2:])      # [40, 50]
print(nums[::2])      # [10, 30, 50]
print(nums[::-1])     # [50, 40, 30, 20, 10]  new reversed copy

# ---- Change ----
nums[0] = 99
print(nums)

# ---- Add ----
fruits = ["apple", "banana"]
fruits.append("cherry")          # end            JS: push
fruits.insert(0, "mango")        # (position, value)
fruits.extend(["kiwi", "lime"])  # add many
print(fruits)

# ---- Remove ----
fruits.remove("banana")          # by value (ValueError if missing)
last = fruits.pop()              # removes + returns the last
first = fruits.pop(0)            # removes + returns index 0
del fruits[0]                    # delete by index
print(fruits, last, first)

# ---- Combine ----
a, b = [1, 2], [3, 4]
print(a + b, [*a, *b])           # both [1, 2, 3, 4]

# ---- Sort and reverse ----
scores = [70, 95, 82, 60]
print(sorted(scores))                 # new list
print(sorted(scores, reverse=True))
scores.sort()                         # changes the original
print(scores)
print(scores.reverse())               # None!  changes in place, returns nothing
print(scores)

# ---- Built-ins ----
prices = [19.99, 5.50, 42.00]
print(sum(prices), min(prices), max(prices), round(sum(prices) / len(prices), 2))
print(scores.index(82), scores.count(70))
print(list(range(1, 6)), list("abc"))

# ---- List comprehension: build a list in one line (JS map + filter) ----
squares = [n * n for n in range(1, 6)]           # [1, 4, 9, 16, 25]
evens = [n for n in range(10) if n % 2 == 0]     # [0, 2, 4, 6, 8]
print(squares, evens)



# ---- Copy trap ----
original = [1, 2, 3]
same = original           # NOT a copy, same list
same.append(4)
print(original)           # [1, 2, 3, 4]
real = original[:]        # real copy (or original.copy())
real.append(5)
print(original, real)


# ======================= EXERCISES =======================
# 1. cities = 5 cities. Print the first, the last, and the middle 3.

def city():
    print("Exercise 1")
    cities = ["Kin", "Brazza", "Paris", "Dubai", "Dallas"]
    print("First:", cities[0])
    print("Last:", cities[-1])
    print("Middle 3:", cities[1:4])

city()

# 2. Append "Kinshasa", insert "Lubumbashi" at the start, print the list.

def app():
    print("Exercise 2")
    cities = ["Kin", "Brazza", "Paris", "Dubai", "Dallas"]
    cities.append("Kinshasa")
    cities.insert(0, "Lubumbashi")
    print(cities)

app()

# 3. Remove one city by name, pop the last one, print what was popped.

def rmv():
    print("Exercise 3")
    cities = ['Lubumbashi', 'Kin', 'Brazza', 'Paris', 'Dubai', 'Dallas', 'Kinshasa']
    cities.remove("Kin")
    popped = cities.pop()
    print("Popped:", popped)
    print(cities)

rmv()

# 4. prices = [12.5, 3.0, 47.25, 8.75]
#    Print the total, the cheapest, the most expensive, the average (2 decimals),
#    and the prices from highest to lowest.

def total():
    print("Exercise 4")
    prices = [12.5, 3.0, 47.25, 8.75]
    print("Total:", sum(prices))
    print("Cheapest:", min(prices))
    print("Most expensive:", max(prices))
    print("Average:", round(sum(prices) / len(prices), 2))
    print("High to low:", sorted(prices, reverse=True))

total()

# 5. Write reverse_list(items) that RETURNS a reversed copy (not None).

def reverse_list(items):
    return items[::-1]

print("Exercise 5")
original_prices = [12.5, 3.0, 47.25, 8.75]
print("Reversed:", reverse_list(original_prices))
print("Original untouched:", original_prices)

# 6. Write add_unique(items, value): append only if not already there, return the list.

def add_unique(items, value):
    if value not in items:
        items.append(value)
    return items

print("Exercise 6")
print(add_unique(["a", "b"], "b"))   # ['a', 'b']
print(add_unique(["a", "b"], "c"))   # ['a', 'b', 'c']

# 7. With a list comprehension, make a list of every price in step 4 over 10.

def over_ten():
    print("Exercise 7")
    prices = [12.5, 3.0, 47.25, 8.75]
    expensive = [p for p in prices if p > 10]
    print(expensive)                 # [12.5, 47.25]

over_ten()


# ======================= PROJECT STEP 3 =======================
# A customer's transactions as a list of amounts (+ = deposit, - = withdrawal):
#   history = [500, -120, 75.5, -40, 1200, -300]
# Using list comprehensions and built-ins, print:
#   - all deposits          [500, 75.5, 1200]
#   - all withdrawals       [-120, -40, -300]
#   - total deposited, total withdrawn, and the final balance (sum of all)
#   - the 3 most recent transactions (last 3, newest first)

def project():
    print("Project step 3")
    history = [500, -120, 75.5, -40, 1200, -300]

    deposits = [t for t in history if t > 0]
    withdrawals = [t for t in history if t < 0]

    print("Deposits:", deposits)                     # [500, 75.5, 1200]
    print("Withdrawals:", withdrawals)               # [-120, -40, -300]
    print("Total deposited:", sum(deposits))         # 1775.5
    print("Total withdrawn:", sum(withdrawals))      # -460
    print("Final balance:", sum(history))            # 1315.5
    print("Last 3, newest first:", history[-3:][::-1])   # [-300, 1200, -40]

project()
