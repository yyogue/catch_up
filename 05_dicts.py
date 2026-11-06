# 05: Dictionaries (JS objects)
# Run: python3 05_dicts.py

# ======================= EXAMPLES =======================
person = {"name": "Youssouf", "age": 28}       # keys need quotes
also = dict(name="Youssouf", age=28)
from_pairs = dict([("name", "Youssouf"), ("age", 28)])
print(person == also == from_pairs)

# ---- Read ----
print(person["name"])
print(person.get("city"))             # None instead of crashing
print(person.get("city", "Unknown"))  # default value
print("age" in person)                # checks KEYS
print(len(person))

# ---- Add / change / remove ----
person["city"] = "Dallas"             # add
person["age"] = 29                    # change
removed = person.pop("age")           # remove + return value
gone = person.pop("zip", None)        # no crash when missing
print(person, removed, gone)
person.update({"job": "Tech", "city": "Hurst"})   # add/change several
print(person)

# ---- Keys, values, items ----
print(list(person.keys()))            # JS Object.keys
print(list(person.values()))          # JS Object.values
print(list(person.items()))           # JS Object.entries -> list of tuples

for key, value in person.items():
    print(f"{key}: {value}")

# ---- zip: two lists -> pairs -> dict ----
keys = ["name", "age", "city"]
values = ["Amina", 31, "Kinshasa"]
print(list(zip(keys, values)))
print(dict(zip(keys, values)))

# ---- Counting with a dict ----
words = ["sql", "python", "sql", "git", "sql"]
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
print(counts)                         # {'sql': 3, 'python': 1, 'git': 1}

# ---- Nested: dict of dicts, list of dicts ----
users = {
    "u1": {"name": "Ana", "age": 25},
    "u2": {"name": "Ben", "age": 30},
}
print(users["u2"]["name"])

people = [{"name": "Ana", "age": 25}, {"name": "Ben", "age": 30}]
for p in people:
    print(p["name"], p["age"])
print(sorted(people, key=lambda p: p["age"], reverse=True)[0]["name"])   # oldest

# ---- Dict comprehension ----
squares = {n: n * n for n in range(1, 5)}
print(squares)


# ======================= EXERCISES =======================
# 1. Make a dict for a car: brand, model, year. Print the model.
#    Add "color", change "year", pop "brand". Print the dict.

# 2. Print get_value(d, key) that returns the value or "Not found".

# 3. Loop over the car dict and print "key -> value" for each item.

# 4. Build a dict from keys = ["a", "b", "c"] and values = [1, 2, 3] using zip.

# 5. Count letters: for "mississippi", build a dict of how many times each letter appears.

# 6. students = [{"name": "Ana", "grade": 88}, {"name": "Ben", "grade": 95}, {"name": "Cy", "grade": 72}]
#    Print the name with the highest grade, and the average grade.


# ======================= PROJECT STEP 5 =======================
# Turn customers into dicts, stored in a "bank" dict keyed by account number:
#   bank = {
#       "ACC-48213907": {"owner": "Youssouf", "balance": 1250.5},
#       "ACC-55102266": {"owner": "Amina", "balance": 300},
#   }
# 1. Add a third account.
# 2. Print every account like: "ACC-48213907 | Youssouf | $1250.50"
# 3. Write total_deposits(bank) that returns the sum of all balances.
# 4. Write find_by_owner(bank, owner) that returns the account number, or None.
