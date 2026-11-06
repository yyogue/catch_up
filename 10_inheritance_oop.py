# 10: Inheritance and the OOP pillars
# Run: python3 10_inheritance_oop.py

from abc import ABC, abstractmethod

# ======================= EXAMPLES =======================

# ---- Inheritance: Dog IS an Animal ----
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

    def describe(self):
        return f"{self.name} says {self.speak()}"


class Dog(Animal):                    # JS: class Dog extends Animal
    def speak(self):                  # override: replaces the parent's version
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


print(Dog("Buddy").describe())        # describe() comes from Animal
print(Cat("Tom").describe())

# ---- super(): child with EXTRA parameters ----
class Puppy(Dog):                     # chain: Animal -> Dog -> Puppy
    def __init__(self, name, breed):
        super().__init__(name)        # let the parent set self.name
        self.breed = breed            # then add your own

    def play(self):
        return f"{self.name} the {self.breed} is playing"


p = Puppy("Max", "Lab")
print(p.play(), p.speak())            # speak() inherited from Dog

# ---- Multiple inheritance ----
class Flyer:
    def fly(self):
        return "Flying high"


class Parrot(Animal, Flyer):
    def speak(self):
        return "Squawk!"


polly = Parrot("Polly")
print(polly.describe(), polly.fly())
print(isinstance(polly, Animal), issubclass(Parrot, Flyer), issubclass(Dog, Flyer))

# ---- Polymorphism: same method name, each class its own way ----
for animal in [Dog("A"), Cat("B"), Parrot("C")]:
    print(animal.speak())

# ---- Abstraction: ABC forces children to write the method ----
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(3.14159 * self.radius ** 2, 2)


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h

    def area(self):
        return self.w * self.h


print([s.area() for s in [Circle(2), Rectangle(3, 4)]])
try:
    Shape()
except TypeError as e:
    print("Can't create Shape:", e)

# ---- Encapsulation: _private data, changed only through methods ----
class BankAccount:
    def __init__(self, number, balance=0):
        self._number = number         # _ = "don't touch from outside"
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount

    def get_balance(self):
        return self._balance


acct = BankAccount("ACC-1", 100)
acct.deposit(50)
acct.withdraw(500)                    # ignored, rules protect the data
print(acct.get_balance())             # 150

# ---- Composition vs inheritance ----
# "Dog IS an Animal"  -> inheritance:  class Dog(Animal)
# "Team HAS users"    -> composition:  self.members = [...]


# ======================= EXERCISES =======================
# 1. Class Vehicle(make, model, year) with display_info().
#    Class Car(Vehicle) that adds fuel_type (use super) and a drive() method.

# 2. Class Employee(name, salary) with pay(). Class Manager(Employee) that adds a bonus
#    and overrides pay() to return salary + bonus.

# 3. Abstract class Payment with abstract method process(amount).
#    Children CardPayment and MobileMoneyPayment return different messages.
#    Loop over a list of both and call process(100) on each (polymorphism).

# 4. Make a Thermostat with a private _temp. set_temp(t) only accepts 60 to 80.


# ======================= PROJECT STEP 10 =======================
# Split your Account class into a family:
# 1. Make Account abstract (ABC) with an abstract method account_type().
#    Rename balance to _balance (encapsulation).
# 2. Checking(Account): account_type() returns "Checking"; every withdraw costs a $1 fee.
#    (override withdraw, call super().withdraw(amount + 1))
# 3. Savings(Account): adds rate (use super().__init__), account_type() returns "Savings",
#    add_interest() adds balance * rate.
# 4. Put one of each in a list, loop and print account_type() and the balance for each.
