# Solutions for 08_errors.py

# 1
def safe_int(text):
    try:
        return int(text)
    except ValueError:
        return 0

print(safe_int("42"), safe_int("abc"))

# 2
def get_item(items, index):
    try:
        return items[index]
    except IndexError:
        return "Out of range"

print(get_item([1, 2], 1), get_item([1, 2], 9))

# 3
def get_key(d, key):
    try:
        return d[key]
    except KeyError:
        return "Missing"

print(get_key({"a": 1}, "a"), get_key({"a": 1}, "b"))

# 4
def check_password(pw):
    if len(pw) < 8:
        raise ValueError("Password must be at least 8 characters")
    return True

try:
    check_password("abc")
except ValueError as e:
    print("Error:", e)

# 5
class NegativeAmountError(Exception):
    pass

def validate_amount(amount):
    if amount < 0:
        raise NegativeAmountError(f"{amount} is negative")
    return amount

try:
    validate_amount(-10)
except NegativeAmountError as e:
    print("Error:", e)

# PROJECT STEP 8
class InsufficientFundsError(Exception):
    pass

class InvalidAmountError(Exception):
    pass

def deposit(acct, amount):
    if amount <= 0:
        raise InvalidAmountError(f"Deposit must be more than 0, got {amount}")
    acct["balance"] += amount

def withdraw(acct, amount):
    if amount <= 0:
        raise InvalidAmountError(f"Withdraw must be more than 0, got {amount}")
    if amount > acct["balance"]:
        raise InsufficientFundsError(f"Only ${acct['balance']:.2f} available")
    acct["balance"] -= amount

acct = {"owner": "Youssouf", "balance": 1000}
actions = [("deposit", 100), ("withdraw", 5000), ("deposit", -20), ("withdraw", 50)]
for kind, amount in actions:
    try:
        if kind == "deposit":
            deposit(acct, amount)
        else:
            withdraw(acct, amount)
        print("OK  ", kind, amount)
    except (InsufficientFundsError, InvalidAmountError) as e:
        print("FAIL", kind, amount, "->", e)
    finally:
        print("     balance:", acct["balance"])
