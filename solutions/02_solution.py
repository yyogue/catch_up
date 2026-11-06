# Solutions for 02_strings.py

# 1
full = "Youssouf Yogue"
print(full[:8])
print(full[9:])

# 2
print(full[::-1])
print(full[::2])

# 3
print("Kinshasa"[-3:])

# 4
name, count, price = "Youssouf", 3, 45
print(f"{name} has {count} classes and pays ${price:.2f} each")

# 5
email = "  YousSouf@Example.COM  "
clean = email.strip().lower()
print(clean)
print(clean.split("@")[0])
print(clean[:clean.find("@")])        # same thing with find + slicing

# 6
def count_vowels(text):
    count = 0
    for char in text:
        if char in "aeiouAEIOU":
            count += 1
    return count

print(count_vowels("Hello World"))

# 7
data = "apple;banana;cherry"
print(", ".join(data.split(";")))

# PROJECT STEP 2
def mask_account(number):
    return "****" + number[-4:]

def format_owner(name):
    return name.strip().title()

print(f"{format_owner('  youssouf YOGUE ')} | {mask_account('ACC-48213907')} | ${1250.5:.2f}")
