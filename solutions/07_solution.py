# Solutions for 07_functions_lambdas.py

# 1
def is_adult(age):
    return age >= 18

print(is_adult(20), is_adult(15))

# 2
def price_with_tax(price, rate=0.0825):
    return round(price * (1 + rate), 2)

print(price_with_tax(100), price_with_tax(100, 0.05))

# 3
def min_max_avg(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

low, high, avg = min_max_avg([4, 8, 15, 16])
print(low, high, avg)

# 4
def average(*numbers):
    return sum(numbers) / len(numbers)

print(average(1, 2, 3), average(10, 20))

# 5
print(sorted(["banana", "kiwi", "apple"], key=lambda w: len(w)))

# 6
print(list(map(lambda n: str(n), [1, 2, 3])))
print(list(filter(lambda w: w.startswith("a"), ["apple", "kiwi", "avocado"])))

# PROJECT STEP 7
def deposit(acct, amount):
    acct["balance"] += amount
    return acct["balance"]

def withdraw(acct, amount):
    if amount > acct["balance"]:
        return False
    acct["balance"] -= amount
    return True

def apply_fee(acct, fee=2.5):
    acct["balance"] -= fee

accounts = [
    {"owner": "Youssouf", "balance": 1000},
    {"owner": "Amina", "balance": 80},
    {"owner": "Ben", "balance": 450},
]
print(deposit(accounts[0], 200), withdraw(accounts[1], 500), withdraw(accounts[2], 50))
apply_fee(accounts[2])

for a in sorted(accounts, key=lambda a: a["balance"], reverse=True):
    print(a["owner"], a["balance"])
print([a["owner"] for a in filter(lambda a: a["balance"] < 100, accounts)])
