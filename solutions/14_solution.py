# Solutions for 14_sql_joins.py
import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.executescript("""
    CREATE TABLE location (id INTEGER PRIMARY KEY AUTOINCREMENT, city TEXT);
    INSERT INTO location (city) VALUES ('Reston'), ('Arlington'), ('Los Angeles'), ('Houston');
    CREATE TABLE employee (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, salary REAL,
        location_id INTEGER REFERENCES location(id));
    INSERT INTO employee (name, salary, location_id) VALUES
        ('Sophie', 67890, 1), ('Ava', 176345, 1), ('Kieran', 124563, 3),
        ('Landon', 53465, 2), ('Xander', 67893, 2), ('Nadia', 61000, NULL);
    CREATE TABLE class (id INTEGER PRIMARY KEY AUTOINCREMENT, teacher_name TEXT, class_title TEXT);
    INSERT INTO class (teacher_name, class_title) VALUES
        ('Ms. Lovelace', 'Physics'), ('Ms. Lovelace', 'Math'), ('Mr. McCarthy', 'Writing'), ('Ms. Goodall', 'Biology');
    CREATE TABLE student (id INTEGER PRIMARY KEY AUTOINCREMENT, student_name TEXT, class_title TEXT);
    INSERT INTO student (student_name, class_title) VALUES
        ('John Stewart', 'Writing'), ('Stephen Colbert', 'Physics'), ('Samantha Bee', 'Math'),
        ('Aasif Mandvi', 'Writing'), ('Robert Riggle', 'Physics'), ('Jessica Williams', 'Art');
""")

def show(sql):
    print("\n>", sql)
    for row in cur.execute(sql).fetchall():
        print("  ", row)

show("SELECT employee.name, location.city FROM employee "
     "INNER JOIN location ON employee.location_id = location.id ORDER BY location.city;")          # 1
show("SELECT employee.name, employee.salary FROM employee "
     "INNER JOIN location ON employee.location_id = location.id "
     "WHERE location.city = 'Los Angeles' AND employee.salary > 100000;")                         # 2
show("SELECT employee.name, location.city FROM employee "
     "LEFT JOIN location ON employee.location_id = location.id;")                                 # 3
show("SELECT class.class_title, COUNT(student.id) FROM class "
     "LEFT JOIN student ON class.class_title = student.class_title GROUP BY class.class_title;")  # 4
show("SELECT student.student_name FROM student "
     "LEFT JOIN class ON student.class_title = class.class_title WHERE class.id IS NULL;")        # 5
show("SELECT location.city, AVG(employee.salary) AS avg_pay FROM employee "
     "INNER JOIN location ON employee.location_id = location.id "
     "GROUP BY location.city ORDER BY avg_pay DESC LIMIT 1;")                                     # 6

# PROJECT STEP 14
bank = sqlite3.connect(":memory:")
bank.executescript("""
    CREATE TABLE account (id INTEGER PRIMARY KEY AUTOINCREMENT,
        owner TEXT, account_number TEXT, type TEXT, balance REAL);
    CREATE TABLE txn (id INTEGER PRIMARY KEY AUTOINCREMENT,
        account_id int REFERENCES account(id), kind TEXT, amount REAL);
    INSERT INTO account (owner, account_number, type, balance) VALUES
        ('Youssouf', 'ACC-48213907', 'Checking', 700),
        ('Amina', 'ACC-55102266', 'Savings', 850),
        ('Ben', 'ACC-77310045', 'Checking', 50);
    INSERT INTO txn (account_id, kind, amount) VALUES
        (1, 'deposit', 200), (1, 'withdraw', 50), (2, 'withdraw', 150);
""")

def statement(conn, account_id):
    return conn.execute("""
        SELECT account.owner, txn.kind, txn.amount
        FROM txn INNER JOIN account ON txn.account_id = account.id
        WHERE account.id = ?;""", (account_id,)).fetchall()

def txn_summary(conn):
    return conn.execute("""
        SELECT account.owner, COUNT(txn.id), SUM(txn.amount)
        FROM account LEFT JOIN txn ON account.id = txn.account_id
        GROUP BY account.id;""").fetchall()

def inactive_accounts(conn):
    return conn.execute("""
        SELECT account.owner
        FROM account LEFT JOIN txn ON account.id = txn.account_id
        WHERE txn.id IS NULL;""").fetchall()

print("\n", statement(bank, 1))
print(txn_summary(bank))
print(inactive_accounts(bank))
