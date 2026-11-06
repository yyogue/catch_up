# Solutions for 05_dicts.py

# 1
car = {"brand": "Toyota", "model": "Camry", "year": 2018}
print(car["model"])
car["color"] = "black"
car["year"] = 2020
car.pop("brand")
print(car)

# 2
def get_value(d, key):
    return d.get(key, "Not found")

print(get_value(car, "model"), get_value(car, "price"))

# 3
for key, value in car.items():
    print(key, "->", value)

# 4
print(dict(zip(["a", "b", "c"], [1, 2, 3])))

# 5
counts = {}
for letter in "mississippi":
    counts[letter] = counts.get(letter, 0) + 1
print(counts)

# 6
students = [{"name": "Ana", "grade": 88}, {"name": "Ben", "grade": 95}, {"name": "Cy", "grade": 72}]
best = max(students, key=lambda s: s["grade"])
print(best["name"])
print(round(sum(s["grade"] for s in students) / len(students), 2))

# PROJECT STEP 5
bank = {
    "ACC-48213907": {"owner": "Youssouf", "balance": 1250.5},
    "ACC-55102266": {"owner": "Amina", "balance": 300},
}
bank["ACC-77310045"] = {"owner": "Ben", "balance": 50}

for number, info in bank.items():
    print(f"{number} | {info['owner']} | ${info['balance']:.2f}")

def total_deposits(bank):
    return sum(info["balance"] for info in bank.values())

def find_by_owner(bank, owner):
    for number, info in bank.items():
        if info["owner"] == owner:
            return number
    return None

print(total_deposits(bank), find_by_owner(bank, "Amina"), find_by_owner(bank, "Zed"))
