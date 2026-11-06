# Solutions for 09_classes.py

# 1, 2, 3
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0

    def description(self):
        return f"{self.year} {self.brand} {self.model}"

    def drive(self, miles):
        self.mileage += miles

    def __str__(self):
        return self.description()

c1 = Car("Toyota", "Camry", 2022)
c2 = Car("Mercedes", "C300", 2016)
print(c1.description(), "/", c2.description())
c1.drive(120)
c1.drive(30)
print(c1.mileage)
print(c2)

# 4
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

r = Rectangle(3, 4)
print(r.area(), r.perimeter())

# 5
class Playlist:
    def __init__(self):
        self.songs = []

    def add(self, song):
        self.songs.append(song)

    def remove(self, song):
        if song in self.songs:
            self.songs.remove(song)

    def count(self):
        return len(self.songs)

pl = Playlist()
pl.add("Kashmir")
pl.add("Africa")
pl.remove("Kashmir")
print(pl.count(), pl.songs)

# PROJECT STEP 9
class Account:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        self.balance += amount
        self.history.append(("deposit", amount))

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        self.balance -= amount
        self.history.append(("withdraw", amount))
        return True

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"{self.owner} | ****{self.account_number[-4:]} | ${self.balance:.2f}"

a1 = Account("Youssouf", "ACC-48213907", 1250.5)
a2 = Account("Amina", "ACC-55102266")
a1.deposit(100)
a1.withdraw(50)
a2.deposit(300)
print(a2.withdraw(1000))
for acct in [a1, a2]:
    print(acct, acct.history)
