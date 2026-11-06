# Solutions for 04_tuples_sets.py

# 1
me = ("Youssouf", 28, "Hurst")
name, age, city = me
print(name, age, city)

# 2
def stats(numbers):
    total = sum(numbers)
    return total, total / len(numbers)

total, average = stats([10, 20, 30])
print(total, average)

# 3
a, b = "first", "second"
a, b = b, a
print(a, b)

# 4
t = (5, 3, 5, 9, 5)
print(t.count(5), t.index(9), t[::-1])

# 5
tags = ["python", "sql", "python", "git", "sql"]
unique = set(tags)
print(unique, len(unique))

# 6
math = {"Ana", "Ben", "Cy"}
art = {"Ben", "Dee"}
print(math & art, math | art, math - art)

# PROJECT STEP 4
txns = [("deposit", 500, "salary"), ("withdraw", 120, "groceries"),
        ("deposit", 75.5, "refund"), ("withdraw", 40, "gas")]

for kind, amount, note in txns:
    print(f"{kind:9} ${amount:>8.2f}  {note}")

def summary(txns):
    total_in = sum(amount for kind, amount, note in txns if kind == "deposit")
    total_out = sum(amount for kind, amount, note in txns if kind == "withdraw")
    return total_in, total_out

total_in, total_out = summary(txns)
print("in:", total_in, "out:", total_out)
print("kinds:", {kind for kind, amount, note in txns})
