# Solutions for 10_inheritance_oop.py
from abc import ABC, abstractmethod

# 1
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type

    def drive(self):
        print("Car is moving")

car = Car("Toyota", "Camry", 2022, "Gasoline")
print(car.display_info(), car.fuel_type)
car.drive()

# 2
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def pay(self):
        return self.salary

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def pay(self):
        return self.salary + self.bonus

print(Employee("Ana", 50000).pay(), Manager("Ben", 70000, 10000).pay())

# 3
class Payment(ABC):
    @abstractmethod
    def process(self, amount):
        pass

class CardPayment(Payment):
    def process(self, amount):
        return f"Charged ${amount} to card"

class MobileMoneyPayment(Payment):
    def process(self, amount):
        return f"Sent ${amount} by mobile money"

for p in [CardPayment(), MobileMoneyPayment()]:
    print(p.process(100))

# 4
class Thermostat:
    def __init__(self):
        self._temp = 70

    def set_temp(self, t):
        if 60 <= t <= 80:
            self._temp = t

    def get_temp(self):
        return self._temp

th = Thermostat()
th.set_temp(95)
th.set_temp(72)
print(th.get_temp())

# PROJECT STEP 10
class Account(ABC):
    def __init__(self, owner, number, balance=0):
        self.owner = owner
        self.number = number
        self._balance = balance
        self.history = []

    @abstractmethod
    def account_type(self):
        pass

    def deposit(self, amount):
        self._balance += amount
        self.history.append(("deposit", amount))

    def withdraw(self, amount):
        if amount > self._balance:
            return False
        self._balance -= amount
        self.history.append(("withdraw", amount))
        return True

    def get_balance(self):
        return self._balance

class Checking(Account):
    def account_type(self):
        return "Checking"

    def withdraw(self, amount):
        return super().withdraw(amount + 1)

class Savings(Account):
    def __init__(self, owner, number, balance=0, rate=0.02):
        super().__init__(owner, number, balance)
        self.rate = rate

    def account_type(self):
        return "Savings"

    def add_interest(self):
        self.deposit(round(self._balance * self.rate, 2))

chk = Checking("Youssouf", "ACC-1", 500)
sav = Savings("Amina", "ACC-2", 1000, 0.05)
chk.withdraw(100)
sav.add_interest()
for acct in [chk, sav]:
    print(acct.account_type(), acct.get_balance())
