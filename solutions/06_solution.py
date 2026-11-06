# Solutions for 06_conditions_loops.py

# 1
def even_or_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

print(even_or_odd(4), even_or_odd(7))

# 2
def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    return "F"

print(grade(95), grade(85), grade(72), grade(40))

# 3
print([n for n in range(1, 21) if n % 3 == 0])

# 4
for i in range(10, 0, -1):
    print(i, end=" ")
print("Go!")

# 5
number, doublings = 1, 0
while number <= 1000:
    number *= 2
    doublings += 1
print(number, "after", doublings, "doublings")

# 6
for n in range(1, 31):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)

# 7
for i, letter in enumerate(["a", "b", "c"], start=1):
    print(f"{i}. {letter}")

# PROJECT STEP 6
balance = 1000
txns = [("deposit", 200), ("withdraw", 1500), ("withdraw", 300), ("bonus", 50), ("deposit", 0)]
for kind, amount in txns:
    if kind == "deposit":
        if amount <= 0:
            print("Skipped deposit of", amount)
            continue
        balance += amount
    elif kind == "withdraw":
        if amount > balance:
            print("DECLINED", amount)
        else:
            balance -= amount
    else:
        print("Unknown type:", kind)
    print("balance:", balance)
print("final balance:", balance)
