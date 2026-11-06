# 01: Variables, types, converting, scope
# Run: python3 01_variables_scope.py

# ======================= EXAMPLES =======================

# ---- Types ----
age = 28                  # int
price = 19.99             # float
is_active = True          # bool (capital T / F)
name = "Youssouf"         # str
nothing = None            # None = no value yet (Python's null)

print(type(age), type(price), type(is_active), type(name), type(nothing))

# ---- Converting ----
print(int("5") + 1)       # 6
print(float("2.5"))       # 2.5
print(str(10) + "0")      # 100   (text glued, not math)
print(int(7.9))           # 7     cuts, does NOT round
print(round(7.9))         # 8     rounds
print(bool(0), bool(1), bool(""), bool("hi"))   # False True False True

# ---- Math operators ----
print(7 + 2, 7 - 2, 7 * 2)  # 9 5 14
print(7 / 2)              # 3.5   always a float
print(7 // 2)             # 3     floor division
print(7 % 2)              # 1     remainder (even/odd checks)
print(2 ** 3)             # 8     power

x = 10
x += 5                    # x = x + 5
x -= 3
x *= 2
print(x)                  # 24

# ---- Scope ----
greeting = "global"       # top of the file = global

def show():
    local_msg = "local"   # only exists inside show()
    print(greeting, local_msg)   # reading a global: fine

show()

count = 0
def increment():
    global count          # needed to CHANGE a global
    count += 1

increment()
increment()
print("count:", count)    # 2

def outer():
    n = 0
    def inner():
        nonlocal n        # needed to CHANGE the outer function's variable
        n += 1
    inner()
    inner()
    return n

print("outer:", outer())  # 2


# ======================= EXERCISES =======================
# 1. Make one variable of each type: int, float, bool, str, None.
#    Print each one next to its type().
sep = "##########" * 2
print(sep + " Sep " + sep)

def ex1():
    var_int = 1
    var_float = 12.4
    var_bol = True
    var_str = "exercise"
    var_none = None

    print(sep + " ex1 " + sep)
    print("int: " , type(var_int))
    print("float: " , type(var_float))
    print("bol: " , type(var_bol))
    print("str: " , type(var_str))
    print("none: " , type(var_none))

ex1()

# 2. Convert "1500" to an int, add 500, print it.
#    Then convert 3.99 to an int and to a rounded int. Print both.

def ex2():
    print(sep + " ex2 " + sep)
    print("1500 + 500:", int("1500") + 500)
    print("int(3.99):", int(3.99))
    print("round(3.99):", round(3.99))

# 3. Use % to print whether 17 is even or odd (hint: 17 % 2).

def ex3(number):
    print(sep + " ex3 " + sep)
    print("Even" if number % 2 == 0 else "Odd")

ex3(17)


# 4. Write make_total() that creates total = 10 inside and prints it.
#    Call it, then try print(total) outside. Read the error, then comment it out.

def make_total():
    print(sep + " ex4 " + sep)
    total = 10
    return total

print(make_total())

visits = 0



# 5. Global visits = 0. Write visit() that adds 1 using global.
#    Call it 3 times. Print visits (should be 3).

def ex5():
    print(sep + " ex5 " + sep)
    global visits
    visits += 1
    return visits 

ex5()
ex5()
ex5()

print("Visits the Global: ", visits)

# ======================= PROJECT STEP 1 =======================
# The bank app starts here. Create these variables for ONE customer:
#   owner = your name, account_number = "ACC-48213907",
#   balance = 1250.5, is_active = True
# Print:  "Youssouf | ACC-48213907 | $1250.50 | active: True"
# (use an f-string with :.2f for the balance)

def project():
    print(sep + " Projects " + sep)
    owner = "Youssouf Yogue"
    account_number = "ACC-48213907"
    balance = 1250.5
    is_active = True

    print(f"{owner} | {account_number} | ${balance:.2f} | active: {is_active}")


project()
