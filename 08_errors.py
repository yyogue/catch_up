# 08: Errors: try / except / raise
# Run: python3 08_errors.py

# ======================= EXAMPLES =======================

# ---- try / except ----
try:
    number = int("abc")
except ValueError:
    print("That's not a number")

# ---- Several kinds, and reading the message ----
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Can't divide by zero")
        return None
    except TypeError as e:
        print("Bad types:", e)
        return None

print(safe_divide(10, 2), safe_divide(10, 0), safe_divide(10, "x"))

# ---- else and finally ----
try:
    value = int("42")
except ValueError:
    print("bad")
else:
    print("no error, value is", value)    # runs only if nothing failed
finally:
    print("finally ALWAYS runs")          # cleanup goes here

# ---- Common errors you'll see ----
tests = [
    lambda: [1, 2][5],          # IndexError
    lambda: {"a": 1}["b"],      # KeyError
    lambda: int("x"),           # ValueError
    lambda: "a" + 1,            # TypeError
    lambda: undefined_name,     # NameError
]
for test in tests:
    try:
        test()
    except Exception as e:      # Exception catches almost everything
        print(type(e).__name__, "->", e)

# ---- Keep asking until valid (pattern from your labs) ----
def to_int(text):
    try:
        return int(text)
    except ValueError:
        return -1

print(to_int("7"), to_int("seven"))

# ---- raise: throw your own error (JS: throw new Error) ----
def set_age(age):
    if age < 0:
        raise ValueError("Age can't be negative")
    return age

try:
    set_age(-5)
except ValueError as e:
    print("Caught:", e)

# ---- Your own error type (inheritance from Exception) ----
class InsufficientFundsError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(f"Need ${amount}, only have ${balance}")
    return balance - amount

try:
    withdraw(50, 80)
except InsufficientFundsError as e:
    print("Declined:", e)


# ======================= EXERCISES =======================
# 1. Write safe_int(text) that returns the int, or 0 if it can't be converted.

# 2. Write get_item(items, index) that returns the item, or "Out of range"
#    (catch IndexError).

# 3. Write get_key(d, key) that catches KeyError and returns "Missing".

# 4. Write check_password(pw) that raises ValueError if pw is shorter than 8 characters,
#    else returns True. Call it inside try/except and print the error message.

# 5. Make your own error class NegativeAmountError and raise it from
#    validate_amount(amount) when amount < 0. Catch it and print it.


# ======================= PROJECT STEP 8 =======================
# Make the bank functions safe with your own errors:
# 1. Create InsufficientFundsError and InvalidAmountError (both inherit from Exception).
# 2. deposit(acct, amount): raise InvalidAmountError if amount <= 0
#    withdraw(acct, amount): raise InvalidAmountError if amount <= 0,
#                            raise InsufficientFundsError if not enough money
# 3. Run this list through them with try/except, printing OK or the error:
#    actions = [("deposit", 100), ("withdraw", 5000), ("deposit", -20), ("withdraw", 50)]
# 4. Use finally to print the balance after every action.
