# Solutions for 01_variables_scope.py

# 1
year = 2026
height = 5.9
likes_python = True
nickname = "You"
pending = None
for value in [year, height, likes_python, nickname, pending]:
    print(value, type(value))

# 2
print(int("1500") + 500)
print(int(3.99), round(3.99))

# 3
print("17 is", "even" if 17 % 2 == 0 else "odd")

# 4
def make_total():
    total = 10
    print(total)

make_total()
# print(total)   # NameError: name 'total' is not defined

# 5
visits = 0
def visit():
    global visits
    visits += 1

visit()
visit()
visit()
print("visits:", visits)

# PROJECT STEP 1
owner = "Youssouf"
account_number = "ACC-48213907"
balance = 1250.5
is_active = True
print(f"{owner} | {account_number} | ${balance:.2f} | active: {is_active}")
