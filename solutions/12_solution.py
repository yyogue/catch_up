# Solutions for 12_sql_basics.py
import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()

# 1
cur.execute("""
    CREATE TABLE dogs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT, breed TEXT, age int
    );
""")

# 2
def insert_dog(cur, name, breed, age):
    cur.execute("INSERT INTO dogs (name, breed, age) VALUES (?, ?, ?);", (name, breed, age))

insert_dog(cur, "Buddy", "Labrador", 3)
insert_dog(cur, "O'Malley", "Beagle", 5)
insert_dog(cur, "Rex", "Husky", 2)
conn.commit()

# 3
def select_all_dogs(cur):
    cur.execute("SELECT * FROM dogs;")
    return cur.fetchall()

print(select_all_dogs(cur))

# 4
cur.execute("UPDATE dogs SET age = ? WHERE name = ?;", (4, "Buddy"))
cur.execute("DELETE FROM dogs WHERE name = ?;", ("Rex",))
conn.commit()
print(select_all_dogs(cur))

# 5
cur.execute("ALTER TABLE dogs ADD owner TEXT;")
cur.execute("UPDATE dogs SET owner = ? WHERE id = ?;", ("Youssouf", 1))
print(select_all_dogs(cur))

# 6
cur.execute("CREATE VIEW dog_names AS SELECT name, breed FROM dogs;")
print(cur.execute("SELECT * FROM dog_names;").fetchall())
conn.close()

# PROJECT STEP 12
def setup_db():
    conn = sqlite3.connect(":memory:")
    conn.execute("PRAGMA foreign_keys = ON;")
    conn.execute("""
        CREATE TABLE account (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            owner TEXT, account_number TEXT, type TEXT, balance REAL
        );
    """)
    conn.execute("""
        CREATE TABLE txn (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            account_id int REFERENCES account(id),
            kind TEXT, amount REAL
        );
    """)
    conn.commit()
    return conn

def save_account(conn, owner, number, kind, balance):
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO account (owner, account_number, type, balance) VALUES (?, ?, ?, ?);",
        (owner, number, kind, balance),
    )
    conn.commit()
    return cur.lastrowid

def log_txn(conn, account_id, kind, amount):
    conn.execute("INSERT INTO txn (account_id, kind, amount) VALUES (?, ?, ?);", (account_id, kind, amount))
    conn.commit()

def update_balance(conn, account_id, new_balance):
    conn.execute("UPDATE account SET balance = ? WHERE id = ?;", (new_balance, account_id))
    conn.commit()

bank = setup_db()
y = save_account(bank, "Youssouf", "ACC-48213907", "Checking", 500)
a = save_account(bank, "Amina", "ACC-55102266", "Savings", 1000)
b = save_account(bank, "Ben", "ACC-77310045", "Checking", 50)
log_txn(bank, y, "deposit", 200)
update_balance(bank, y, 700)
log_txn(bank, a, "withdraw", 150)
update_balance(bank, a, 850)
print(bank.execute("SELECT * FROM account;").fetchall())
print(bank.execute("SELECT * FROM txn;").fetchall())
