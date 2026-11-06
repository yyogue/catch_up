# 02: Strings
# Run: python3 02_strings.py

# ======================= EXAMPLES =======================
city = "Dallas"
#       012345

# ---- Indexing and slicing:  [start:end:step], end NOT included ----
print(city[0])            # D
print(city[-1])           # s      negative = from the end
print(city[0:3])          # Dal
print(city[2:])           # llas   from 2 to the end
print(city[:2])           # Da     from the start to 2
print(city[-3:])          # las    last 3
print(city[::2])          # Dla    every 2nd letter
print(city[::-1])         # sallaD reversed
print(city[1:5:2])        # al     from 1 to 5, step 2
print(len(city))          # 6
# city[0] = "d"           # TypeError: strings can't be changed

# ---- f-strings ----
name, age, price = "Youssouf", 28, 19.5
print(f"{name} is {age}")
print(f"Total: {price * 3:.2f}")    # 58.50
print(f"{name.upper()} has {len(name)} letters")

# ---- Case ----
print("hello world".upper(), "HELLO".lower(), "hello world".title(), "hello".capitalize())

# ---- Searching ----
print(city.find("a"))     # 1     -1 if missing
print(city.index("a"))    # 1     crashes if missing
print(city.count("a"))    # 2
print("Dal" in city)      # True
print(city.startswith("Da"), city.endswith("as"))

# ---- Changing (returns a NEW string) ----
print(city.replace("l", "L"))         # DaLLas  (ALL of them)
print(city.replace("l", "L", 1))      # DaLlas  (only the first)
print("  hi  ".strip() + "|")         # hi|
print("ha" * 3)                       # hahaha

# ---- Checking content ----
print("123".isdigit(), "abc".isalpha(), "a1".isalnum(), "   ".isspace())

# ---- split and join ----
line = "Youssouf,28,Dallas"
parts = line.split(",")               # ['Youssouf', '28', 'Dallas']
print(parts)
print(" | ".join(parts))              # separator FIRST (JS is the opposite)
first, age_txt, home = line.split(",")   # split + unpack in one line
print(first, int(age_txt) + 1, home)

# ---- Real examples ----
phone = "(214) 555-0187"
print(phone.replace("(", "").replace(")", "").replace("-", "").replace(" ", ""))
print("My First Blog Post".lower().replace(" ", "-"))   # url slug

def is_palindrome(word):
    clean = "".join(c.lower() for c in word if c.isalnum())
    return clean == clean[::-1]

print(is_palindrome("Racecar"), is_palindrome("A man, a plan, a canal: Panama"), is_palindrome("hello"))


# ======================= EXERCISES =======================
full = "Youssouf Yogue"
#    Using ONLY slicing, print the first name, then the last name.


def slicing():
    print("Exercise: 1")

    f_name = full[0:8]
    l_name = full[9:]

    print("First", f_name)
    print("Last", l_name)

slicing()


# 2. Print full backwards. Then print every 2nd letter of full.

def backwards():
    name = "Youssouf Yogue"
    print(name[::2])
    print(name[::-1])

backwards()

# 3. Print the last 3 letters of "Kinshasa" using a negative slice.

def negative():
    name = "Kinshasa"
    print(name[-3:])

negative()

# 4. With an f-string print: "Youssouf has 3 classes and pays $45.00 each"
#    (variables for name, count, and price = 45)

def strngs():
    name = "Youssouf"
    count = 3
    price = 45
    print(f"{name} has {count} classes and pays ${price:.2f} each")

strngs()

# 5. email = "  YousSouf@Example.COM  " -> clean it (no spaces, all lowercase).
#    Then print only the part before the @ (hint: split or find + slicing).
def five():
    email = "  YousSouf@Example.COM  " 
    spl = email.strip().lower().split("@")
    print("Before: ", email)
    print(email.strip().lower())
    print("Split: ", spl[0])

five()


# 6. Write count_vowels(text) that returns how many vowels are in text
#    (both upper and lower case). Test with "Hello World" -> 3.

def count_vowels(text):
    count = 0
    for char in text:
        if char in "aeiouAEIOU":
            count += 1
    return count

print(count_vowels("Hello World"))   # 3
print(count_vowels("Youssouf"))      # 4

# 7. data = "apple;banana;cherry" -> split it, then join it back with ", ".

def split_join():
    data = "apple;banana;cherry"
    spl = data.split(";")
    joins = ", ".join(spl)
    print("Data: ", data)
    print("Split: ", spl)
    print("Join: ", joins)

split_join()


# ======================= PROJECT STEP 2 =======================
# Banks never show the full account number.
# Write mask_account(number) that turns "ACC-48213907" into "****3907"
# (4 stars + the last 4 characters, using a negative slice).
# Write format_owner(name) that turns "  youssouf YOGUE " into "Youssouf Yogue".
# Print:  "Youssouf Yogue | ****3907 | $1250.50"


def mask_account(number):
    return "****" + number[-4:]

def format_owner(name):
    return name.strip().title()

def project():
    account = "ACC-48213907"
    name = "  youssouf YOGUE "
    amount = 1250.5
    print(f"{format_owner(name)} | {mask_account(account)} | ${amount:.2f}")

project()
# Youssouf Yogue | ****3907 | $1250.50
