# 06: Conditions and loops
# Run: python3 06_conditions_loops.py

# ======================= EXAMPLES =======================

# ---- if / elif / else ----
score = 82
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"
print(grade)

# one-liner (JS:  cond ? a : b)
label = "even" if score % 2 == 0 else "odd"
print(label)

# ---- Comparisons and logic ----
age, has_id = 20, True
print(age >= 18 and has_id)   # JS &&
print(age < 18 or has_id)     # JS ||
print(not has_id)             # JS !
print(18 <= age <= 30)        # chained comparison
print(age != 21)

# ---- Truthy / falsy: 0, "", [], {}, None are False ----
items = []
if not items:
    print("list is empty")

# ---- while ----
count = 0
while count < 3:
    print("count is", count)
    count += 1

is_game_over = False
score = 0
while not is_game_over:       # "while the game is NOT over"
    score += 2
    if score >= 6:
        is_game_over = True
print("final score", score)

# ---- for + range(start, stop, step), stop NOT included ----
for i in range(3):            # 0 1 2
    print(i, end=" ")
print()
for i in range(1, 6):         # 1 2 3 4 5
    print(i, end=" ")
print()
for i in range(10, 0, -2):    # 10 8 6 4 2
    print(i, end=" ")
print()

# ---- Loop over things ----
for letter in "abc":
    print(letter, end=" ")
print()
for i, fruit in enumerate(["apple", "kiwi"]):    # index + value
    print(i, fruit)
for name, age in zip(["Ana", "Ben"], [25, 30]):  # two lists together
    print(name, age)

# ---- break and continue ----
for n in range(1, 10):
    if n == 3:
        continue              # skip this one, keep looping
    if n == 6:
        break                 # stop the loop completely
    print(n, end=" ")
print()

# ---- Classic patterns ----
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def count_digits(num):
    num = abs(num)
    if num == 0:
        return 1
    count = 0
    while num != 0:
        count += 1
        num //= 10
    return count

print(factorial(5), count_digits(-12345))


# ======================= EXERCISES =======================
# 1. Write even_or_odd(n) that returns "Even" or "Odd".

def even_or_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print("Test 39:", even_or_odd(39))
print("Test 40:", even_or_odd(40))

# 2. Write a grade function: 90+ "A", 80+ "B", 70+ "C", else "F".

def grade_function(gd):
    if gd >= 90:
        return "A"
    elif gd >= 80:
        return "B"
    elif gd >= 70:
        return "C"
    else:
        return "F"

print(grade_function(89.99))

# 3. Print the numbers 1 to 20 that can be divided by 3 (use range and %).

def can_be_divided():
    for i in range(1, 21):
        if i % 3 == 0:
            print("Can be divided: ", i)

can_be_divided()

# 4. Print a countdown from 10 to 1 with range and a negative step, then "Go!".

def count_down():
    for i in range(10, 0, -1):
        print(i)
    print("GO!")

count_down()

# 5. Use a while loop to keep doubling a number starting at 1 until it's over 1000.
#    Print how many doublings it took.

def while_function():
    i = 1
    count_double = 0

    while i <= 1000:
        i *= 2
        count_double += 1

    print(f"{count_double} doublings, ended at {i}")

while_function()


# 6. FizzBuzz 1 to 30: multiples of 3 -> "Fizz", of 5 -> "Buzz", both -> "FizzBuzz".

def fizz_buzz():
    for n in range(1, 31):
        if n % 3 == 0 and n % 5 == 0:   # check BOTH first, or 15 would stop at "Fizz"
            print("FizzBuzz")
        elif n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")
        else:
            print(n)

fizz_buzz()

# 7. Loop over ["a", "b", "c"] with enumerate and print "1. a", "2. b", "3. c".

def loop_over():
    array1 = ["a", "b", "c"]

    for index, value in enumerate(array1, start=1):
        print(f"{index}. {value}")

loop_over()


# ======================= PROJECT STEP 6 =======================
# Process transactions one by one and keep a running balance.
#   balance = 1000
#   txns = [("deposit", 200), ("withdraw", 1500), ("withdraw", 300), ("bonus", 50), ("deposit", 0)]
# Rules:
#   - "deposit": add it, but skip (continue) if the amount is 0 or less
#   - "withdraw": only if the balance is enough, else print "DECLINED"
#   - anything else: print "Unknown type"
# Print the balance after each step, and the final balance at the end.

def project():
    balance = 1000
    txns = [("deposit", 200), ("withdraw", 1500), ("withdraw", 300), ("bonus", 50), ("deposit", 0)]

    for kind, amount in txns:
        if kind == "deposit":
            if amount <= 0:
                print(f"Skipped deposit of {amount}")
                continue
            balance += amount
            print(f"Deposited {amount}")
        elif kind == "withdraw":
            if amount > balance:
                print(f"DECLINED withdraw of {amount}")
            else:
                balance -= amount
                print(f"Withdrew {amount}")
        else:
            print(f"Unknown type: {kind}")
        print(f"  balance: {balance}")

    print(f"Final balance: {balance}")

project()
