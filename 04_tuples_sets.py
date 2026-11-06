# 04: Tuples and sets
# Run: python3 04_tuples_sets.py

# ======================= EXAMPLES =======================

# ---- Tuples: a list you can't change ----
point = (10, 20)
also_tuple = 10, 20           # the commas make the tuple
single = (5,)                 # one item needs the trailing comma
print(point[0], len(point), point == also_tuple, type(single))
# point[0] = 5                # TypeError

# ---- Unpacking ----
x, y = point
print(x, y)
person = ("Youssouf", 28, "Dallas")
name, age, city = person
print(f"{name} is {age} and lives in {city}")

first, *rest = (1, 2, 3, 4)   # * collects the rest into a list
print(first, rest)
a, b = 1, 2
a, b = b, a                   # swap
print(a, b)

# ---- Returning 2 values = returning a tuple ----
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3, 8, 1, 9])
print(low, high)

# ---- Tuple methods (only 2) ----
t = ("a", "b", "a", "c")
print(t.count("a"), t.index("c"))
print(t[::-1], t[1:3])        # slicing works like lists
print(t + ("d",), t * 2)      # makes NEW tuples

# ---- Tuples as dict keys (lists can't be keys) ----
rates = {("USD", "CDF"): 2800, ("EUR", "CDF"): 3050}
print(rates[("USD", "CDF")])

# ---- "Editing" a tuple: list, change, back to tuple ----
t2 = (1, 2, 3)
temp = list(t2)
temp.append(4)
t2 = tuple(temp)
print(t2)

# ---- Sets: no duplicates, no order, no index ----
colors = {"red", "green", "red"}
print(colors)                 # {'red', 'green'}
empty_set = set()             # {} would be an empty DICT
colors.add("blue")
colors.discard("pink")        # no error if missing (remove() would crash)
print("red" in colors, len(colors))

emails = ["a@x.com", "b@x.com", "a@x.com"]
print(set(emails))            # duplicates gone

# seen-before check
seen = set()
for e in emails:
    if e in seen:
        print("duplicate:", e)
    seen.add(e)

# compare two groups
team_a = {"Ana", "Ben", "Carl"}
team_b = {"Ben", "Dan"}
print(team_a | team_b)        # everyone
print(team_a & team_b)        # in both
print(team_a - team_b)        # only in team_a


# ======================= EXERCISES =======================
# 1. Make a tuple with your name, age, and city. Unpack it into 3 variables, print them.

def me():
    mine = "Youssouf", 29, "Hurst"
    x, y, z = mine
    print("Unpacking: ", x)
    print("Unpacking: ", y)
    print("Unpacking: ", z)
    print("All: ", x, y, z)

me()

# 2. Write stats(numbers) that returns (total, average). Unpack the result and print both.

def stats(numbers):


# 3. Swap two variables in one line.

# 4. t = (5, 3, 5, 9, 5). Print how many 5s, the index of 9, and the tuple reversed.

# 5. tags = ["python", "sql", "python", "git", "sql"]
#    Print the unique tags, and how many unique there are.

# 6. Two sets of students: math = {...}, art = {...}
#    Print who takes both, who takes either, and who takes only math.


# ======================= PROJECT STEP 4 =======================
# Store transactions as tuples: (kind, amount, note)
#   txns = [("deposit", 500, "salary"), ("withdraw", 120, "groceries"),
#           ("deposit", 75.5, "refund"), ("withdraw", 40, "gas")]
# 1. Loop with unpacking (for kind, amount, note in txns) and print each one like:
#       deposit   $500.00  salary
# 2. Write summary(txns) that RETURNS (total_in, total_out). Unpack and print it.
# 3. Use a set to print which kinds of transactions exist (no duplicates).
