# 09: Classes
# Run: python3 09_classes.py

# ======================= EXAMPLES =======================

class Lightbulb:
    def __init__(self, state):        # constructor (JS: constructor)
        self.state = state            # self = this. self.x = the object remembers it

    def get_state(self):              # getter
        return self.state

    def set_state(self, state):       # setter
        self.state = state

    def get_description(self):
        return "The bulb is on" if self.state else "The bulb is off"


bulb = Lightbulb(True)                # no "new" keyword
print(bulb.get_description())
bulb.set_state(False)
print(bulb.get_state(), bulb.get_description())


class User:
    # class attribute: shared by ALL users
    count = 0

    def __init__(self, name, email, age=None):
        self.name = name              # every property is created in __init__
        self.email = email
        self.age = age                # None = no value yet
        self.is_active = True         # default, not passed in
        User.count += 1

    def deactivate(self):             # action method: changes the object
        self.is_active = False

    def get_description(self):
        status = "active" if self.is_active else "inactive"
        return f"{self.name} ({self.email}), {status}"

    def __str__(self):                # what print(user) shows
        return self.get_description()


u1 = User("Youssouf", "you@example.com", 28)
u2 = User("Ana", "ana@example.com")
u2.deactivate()
print(u1)
print(u2)
print(u1.name, u2.age, User.count)

# list of objects
users = [u1, u2, User("Ben", "ben@example.com", 40)]
for u in users:
    print(u.name, u.is_active)
active_names = [u.name for u in users if u.is_active]
print(active_names)

# composition: an object holding another object ("has a")
class Team:
    def __init__(self, name):
        self.name = name
        self.members = []            # a list of User objects

    def add(self, user):
        self.members.append(user)

    def size(self):
        return len(self.members)

team = Team("Data")
team.add(u1)
team.add(u2)
print(team.name, team.size(), team.members[0].name)


# ======================= EXERCISES =======================
# 1. Create a class Car with brand, model, year. Add a method description()
#    that returns "2022 Toyota Camry". Create 2 cars, print both descriptions.

# 2. Add a property mileage that starts at 0 (not passed in) and a method
#    drive(miles) that adds to it. Drive twice, print the mileage.

# 3. Add __str__ to Car so print(car) shows the description.

# 4. Create a class Rectangle with width and height, and methods area() and perimeter().

# 5. Create a class Playlist that HAS a list of song titles, with add(song),
#    remove(song), and count() methods.


# ======================= PROJECT STEP 9 =======================
# Turn the account dict into a class.
# class Account:
#   __init__(self, owner, account_number, balance=0)  also: self.history = []
#   deposit(amount)   -> adds, appends ("deposit", amount) to history
#   withdraw(amount)  -> subtracts if enough money, appends ("withdraw", amount), returns True
#                        otherwise returns False and changes nothing
#   get_balance()
#   __str__ -> "Youssouf | ****3907 | $1250.50"   (reuse your mask from step 2)
# Create 2 accounts, do a few deposits and withdrawals, print them and their history.
