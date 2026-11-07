# 07: Functions and lambdas
# Run: python3 07_functions_lambdas.py

# ======================= EXAMPLES =======================

# ---- def, parameters, return ----
def add(a, b):
    return a + b

print(add(2, 3))

def say_hi(name):
    print(f"Hi {name}")       # prints, returns nothing

result = say_hi("Ana")
print(result)                 # None: a function with no return gives None

# ---- Default values ----
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Ben"), greet("Ben", "Bonjour"))

# ---- Keyword arguments: name them, any order ----
def make_user(name, age, city="Dallas"):
    return {"name": name, "age": age, "city": city}

print(make_user(age=28, name="Youssouf"))

# ---- Returning several values (a tuple) ----
def divide(a, b):
    return a // b, a % b

quotient, remainder = divide(17, 5)
print(quotient, remainder)

# ---- *args and **kwargs ----
def total(*numbers):          # any number of arguments, arrives as a tuple
    return sum(numbers)

def show(**info):             # any keyword arguments, arrives as a dict
    for k, v in info.items():
        print(k, "=", v)

print(total(1, 2, 3, 4))
show(name="Ana", age=25)

# ---- Functions are values ----
def shout(text):
    return text.upper()

def apply(func, value):
    return func(value)

print(apply(shout, "hey"))

# ---- lambda: one-line function (JS arrow function) ----
double = lambda x: x * 2
add2 = lambda a, b: a + b
print(double(5), add2(3, 4))

# ---- map, filter, sorted ----
nums = [5, 2, 8, 1]
print(list(map(lambda n: n * 10, nums)))           # JS map
print(list(filter(lambda n: n > 2, nums)))         # JS filter
print(sorted(nums), sorted(nums, reverse=True))

products = [("phone", 800), ("case", 20), ("charger", 35)]
print(sorted(products, key=lambda p: p[1]))        # sort by price
print(max(products, key=lambda p: p[1]))           # most expensive

# same thing with list comprehensions (usually more Pythonic)
print([n * 10 for n in nums])
print([n for n in nums if n > 2])

# ---- Docstrings ----
def area(width, height):
    """Returns the area of a rectangle."""
    return width * height

print(area(3, 4), area.__doc__)


# ======================= EXERCISES =======================
# 1. Write is_adult(age) that returns True or False.

def is_adult(age):
    if age:
        return True
    else:
        return False

print(is_adult(20))


# 2. Write price_with_tax(price, rate=0.0825) that returns the price with tax, rounded to 2 decimals.
#    Call it with and without a rate.

def price_with_tax(price, rate=0.0825):
    result = price + rate
    return round(result, 2) 

# 3. Write min_max_avg(numbers) that returns 3 values. Unpack them and print them.

def min_max_avg(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)

    return minimum, maximum, average

print(min_max_avg([70, 85, 90, 65, 100]))

# 4. Write average(*numbers) that works with any amount of numbers.

def average(*numbers):
    return sum(numbers) / len(numbers)

print(average(10, 20))
print(average(10, 20, 30))
print(average(10, 20, 30, 40, 50))

# 5. With a lambda and sorted, sort ["banana", "kiwi", "apple"] by length.

sorting = sorted(["banana", "kiwi", "apple"], key=lambda word: len(word))

print("Sorting:", sorting)

# 6. With map + lambda, turn [1, 2, 3] into ["1", "2", "3"].
#    With filter + lambda, keep only the words starting with "a" from ["apple", "kiwi", "avocado"].

to_turn = [1, 2, 3]
words = ["apple", "kiwi", "avocado"]

six_one = list(map(lambda strgs: str(strgs), to_turn))
six_two = list(filter(lambda x: x.startswith("a"), words))


print("String: ", six_one)
print("Filter: ", six_two)


# ======================= PROJECT STEP 7 =======================
# Turn the bank logic into functions that work on an account dict:
#   acct = {"owner": "Youssouf", "balance": 1000}
# 1. deposit(acct, amount)  -> adds amount, returns the new balance
# 2. withdraw(acct, amount) -> subtracts if enough money, returns True; else returns False
# 3. apply_fee(acct, fee=2.5) -> subtracts a fee (default 2.5)
# 4. accounts = [ {...}, {...}, {...} ]  (3 accounts)
#    With sorted + lambda, print the accounts from richest to poorest.
#    With filter + lambda, print only accounts with less than $100.



def deposit(acct, amount):
    acct["balance"] += amount
    return acct["balance"]


def withdraw(acct, amount):
    if acct["balance"] >= amount:
        acct["balance"] -= amount
        return True
    else:
        return False


def apply_fee(acct, fee=2.5):
    acct["balance"] -= fee
    return acct["balance"]


acct = {"owner": "Youssouf", "balance": 1000}

print(deposit(acct, 200))
print(withdraw(acct, 300))
print(apply_fee(acct))
print(acct)
