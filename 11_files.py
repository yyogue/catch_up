# 11: Files
# Run: python3 11_files.py

import os

# ======================= EXAMPLES =======================

# ---- Write: "w" creates the file, or WIPES it if it exists ----
with open("notes.txt", "w") as f:     # with = closes the file automatically
    f.write("first line\n")           # \n = new line
    f.write("second line\n")

# ---- Append: "a" adds to the end, keeps what's there ----
with open("notes.txt", "a") as f:
    f.write("third line\n")

# ---- Read the whole file as one string ----
with open("notes.txt", "r") as f:     # "r" is the default
    content = f.read()
print(content)

# ---- Read as a list of lines ----
with open("notes.txt") as f:
    lines = f.readlines()
print(lines)                          # ['first line\n', ...]

# ---- Loop line by line (best for big files) ----
with open("notes.txt") as f:
    for number, line in enumerate(f, start=1):
        print(number, line.strip())   # strip removes the \n

# ---- Write a list ----
cities = ["Dallas", "Kinshasa", "Paris"]
with open("cities.txt", "w") as f:
    f.write("\n".join(cities))

with open("cities.txt") as f:
    print(f.read().split("\n"))

# ---- A simple CSV by hand ----
rows = [("Ana", 25), ("Ben", 30)]
with open("people.csv", "w") as f:
    f.write("name,age\n")
    for name, age in rows:
        f.write(f"{name},{age}\n")

with open("people.csv") as f:
    header = f.readline().strip().split(",")
    for line in f:
        name, age = line.strip().split(",")
        print(dict(zip(header, [name, int(age)])))

# ---- Missing file ----
try:
    with open("does_not_exist.txt") as f:
        f.read()
except FileNotFoundError:
    print("File not found")

print(os.path.exists("notes.txt"))

# clean up the example files
for name in ["notes.txt", "cities.txt", "people.csv"]:
    os.remove(name)


# ======================= EXERCISES =======================
# 1. Write 3 of your goals to goals.txt, one per line. Read it back and print it.

# 2. Append a 4th goal without erasing the others. Print the file again.

# 3. Read goals.txt with readlines() and print how many lines it has.

# 4. Write write_to_file(filename, content) that returns True if anything was written,
#    False on error (try/except). Then read_file(filename) that returns the text,
#    or None if the file doesn't exist.

# 5. Write a scores.csv with name,score for 3 people. Read it back and print the average score.


# ======================= PROJECT STEP 11 =======================
# Save and load the bank to a file.
# 1. save_accounts(accounts, filename) writes one line per account:
#       owner,account_number,type,balance
# 2. load_accounts(filename) reads it back and returns a list of dicts.
#    If the file doesn't exist, return an empty list.
# 3. print_statement(account, filename) writes a statement: a header line,
#    then one line per transaction in the account's history, then the final balance.
