# Solutions for 13_sql_queries.py
import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.executescript("""
    CREATE TABLE employee (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT, last_name TEXT, salary REAL, dept TEXT
    );
    INSERT INTO employee (first_name, last_name, salary, dept) VALUES
        ('Steve',   'Garcia', 67400.00,  'Sales'),
        ('Alexa',   'Smith',  42500.00,  'Support'),
        ('Steve',   'Jones',  99890.99,  'Tech'),
        ('Brandon', 'Smith',  120000.00, 'Tech'),
        ('Adam',    'Jones',  55050.50,  'Sales'),
        ('Casey',   'Turner', 75000.00,  'Support'),
        ('Jordan',  'Reyes',  100000.00, 'Tech');
""")

def show(sql, params=()):
    print("\n>", sql)
    for row in cur.execute(sql, params).fetchall():
        print("  ", row)

show("SELECT * FROM employee WHERE dept = 'Tech' AND salary > 100000;")                 # 1
show("SELECT * FROM employee WHERE dept != 'Sales' ORDER BY salary ASC;")              # 2
show("SELECT * FROM employee WHERE last_name LIKE 'J%';")                              # 3
show("SELECT * FROM employee ORDER BY salary ASC LIMIT 1;")                            # 4
show("SELECT COUNT(*), SUM(salary) FROM employee;")                                    # 5
show("SELECT dept, ROUND(AVG(salary), 2) FROM employee GROUP BY dept;")                # 6
show("SELECT dept, COUNT(*) FROM employee GROUP BY dept HAVING COUNT(*) > 2;")         # 7

# PROJECT STEP 13
def setup_db():
    conn = sqlite3.connect(":memory:")
    conn.executescript("""
        CREATE TABLE account (id INTEGER PRIMARY KEY AUTOINCREMENT,
            owner TEXT, account_number TEXT, type TEXT, balance REAL);
        CREATE TABLE txn (id INTEGER PRIMARY KEY AUTOINCREMENT,
            account_id int REFERENCES account(id), kind TEXT, amount REAL);
    """)
    return conn

def save_account(conn, owner, number, kind, balance):
    cur = conn.execute(
        "INSERT INTO account (owner, account_number, type, balance) VALUES (?, ?, ?, ?);",
        (owner, number, kind, balance))
    conn.commit()
    return cur.lastrowid

def log_txn(conn, account_id, kind, amount):
    conn.execute("INSERT INTO txn (account_id, kind, amount) VALUES (?, ?, ?);", (account_id, kind, amount))
    conn.commit()

def richest_account(conn):
    return conn.execute("SELECT owner, balance FROM account ORDER BY balance DESC LIMIT 1;").fetchone()

def total_money(conn):
    return conn.execute("SELECT SUM(balance) FROM account;").fetchone()[0]

def count_by_type(conn):
    return conn.execute("SELECT type, COUNT(*) FROM account GROUP BY type;").fetchall()

def big_withdrawals(conn, limit):
    return conn.execute(
        "SELECT * FROM txn WHERE kind = 'withdraw' AND amount > ? ORDER BY amount DESC;", (limit,)
    ).fetchall()

bank = setup_db()
y = save_account(bank, "Youssouf", "ACC-48213907", "Checking", 700)
a = save_account(bank, "Amina", "ACC-55102266", "Savings", 850)
b = save_account(bank, "Ben", "ACC-77310045", "Checking", 50)
log_txn(bank, y, "withdraw", 300)
log_txn(bank, a, "withdraw", 150)
log_txn(bank, b, "withdraw", 20)
print("\n", richest_account(bank), total_money(bank), count_by_type(bank), big_withdrawals(bank, 100))
