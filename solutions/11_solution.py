# Solutions for 11_files.py
import os

# 1
with open("goals.txt", "w") as f:
    f.write("Finish Revature pre-training\n")
    f.write("Master SQL joins\n")
    f.write("Build the bank project\n")
with open("goals.txt") as f:
    print(f.read())

# 2
with open("goals.txt", "a") as f:
    f.write("Pass the assessment\n")
with open("goals.txt") as f:
    print(f.read())

# 3
with open("goals.txt") as f:
    print(len(f.readlines()), "lines")

# 4
def write_to_file(filename, content):
    try:
        with open(filename, "w") as f:
            f.write(content)
            return f.tell() > 0
    except Exception as e:
        print("Error:", e)
        return False

def read_file(filename):
    try:
        with open(filename) as f:
            return f.read()
    except FileNotFoundError:
        return None

print(write_to_file("hello.txt", "Hi"), read_file("hello.txt"), read_file("nope.txt"))

# 5
with open("scores.csv", "w") as f:
    f.write("name,score\nAna,88\nBen,95\nCy,72\n")
scores = []
with open("scores.csv") as f:
    f.readline()                       # skip the header
    for line in f:
        name, score = line.strip().split(",")
        scores.append(int(score))
print(round(sum(scores) / len(scores), 2))

# PROJECT STEP 11
accounts = [
    {"owner": "Youssouf", "number": "ACC-48213907", "type": "Checking", "balance": 1250.5,
     "history": [("deposit", 200), ("withdraw", 50)]},
    {"owner": "Amina", "number": "ACC-55102266", "type": "Savings", "balance": 300, "history": []},
]

def save_accounts(accounts, filename):
    with open(filename, "w") as f:
        for a in accounts:
            f.write(f"{a['owner']},{a['number']},{a['type']},{a['balance']}\n")

def load_accounts(filename):
    if not os.path.exists(filename):
        return []
    result = []
    with open(filename) as f:
        for line in f:
            owner, number, kind, balance = line.strip().split(",")
            result.append({"owner": owner, "number": number, "type": kind, "balance": float(balance)})
    return result

def print_statement(account, filename):
    with open(filename, "w") as f:
        f.write(f"Statement for {account['owner']} ({account['number'][-4:]})\n")
        for kind, amount in account["history"]:
            f.write(f"{kind:10} ${amount:.2f}\n")
        f.write(f"Balance: ${account['balance']:.2f}\n")

save_accounts(accounts, "bank.txt")
print(load_accounts("bank.txt"))
print(load_accounts("missing.txt"))
print_statement(accounts[0], "statement.txt")
print(read_file("statement.txt"))

for name in ["goals.txt", "hello.txt", "scores.csv", "bank.txt", "statement.txt"]:
    os.remove(name)
