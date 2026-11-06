# 13: SQL queries: filtering, sorting, aggregates, GROUP BY
# Run: python3 13_sql_queries.py

import sqlite3

# ======================= SETUP =======================
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


# ======================= EXAMPLES =======================

# ---- WHERE: =  !=  >  <  >=  <= ----
show("SELECT first_name, salary FROM employee WHERE salary > 75000;")   # Casey (75000) is NOT included
show("SELECT first_name, salary FROM employee WHERE salary >= 75000;")  # now she is
show("SELECT * FROM employee WHERE last_name != 'Smith';")

# ---- AND / OR / NOT IN / IN / BETWEEN ----
show("SELECT * FROM employee WHERE first_name = 'Steve' AND salary > 75000;")
show("SELECT * FROM employee WHERE salary > 100000 OR salary < 50000;")
show("SELECT * FROM employee WHERE dept IN ('Sales', 'Support');")
show("SELECT * FROM employee WHERE first_name NOT IN ('Steve');")
show("SELECT * FROM employee WHERE salary BETWEEN 50000 AND 80000;")     # both ends included

# ---- LIKE: % = anything ----
show("SELECT first_name FROM employee WHERE first_name LIKE 'S%';")     # starts with S
show("SELECT first_name FROM employee WHERE last_name LIKE '%s';")      # ends with s

# ---- ? placeholders with filters ----
show("SELECT * FROM employee WHERE dept = ? AND salary > ?;", ("Tech", 99000))

# ---- ORDER BY and LIMIT (LIMIT always last) ----
show("SELECT first_name, salary FROM employee ORDER BY salary DESC;")
show("SELECT first_name, last_name FROM employee ORDER BY last_name ASC, first_name ASC;")
show("SELECT first_name, salary FROM employee ORDER BY salary DESC LIMIT 2;")   # top 2

# ---- Aggregates: many rows -> one value ----
show("SELECT COUNT(*) FROM employee;")
show("SELECT SUM(salary), AVG(salary), MIN(salary), MAX(salary) FROM employee;")
show("SELECT COUNT(*) FROM employee WHERE last_name = 'Smith';")
show("SELECT COUNT(DISTINCT dept) FROM employee;")        # different values only
total = cur.execute("SELECT SUM(salary) FROM employee;").fetchone()[0]
print("total in Python:", round(total, 2))                # fetchone()[0] pulls the number out

# ---- AS: name a result column ----
show("SELECT ROUND(AVG(salary), 2) AS avg_salary FROM employee;")

# ---- GROUP BY: one result per group ----
show("SELECT dept, COUNT(*) AS people FROM employee GROUP BY dept;")
show("SELECT dept, ROUND(AVG(salary), 2) AS avg_pay FROM employee GROUP BY dept ORDER BY avg_pay DESC;")

# ---- HAVING: filter GROUPS (WHERE filters rows) ----
show("SELECT dept, AVG(salary) FROM employee GROUP BY dept HAVING AVG(salary) > 70000;")

# Full order of clauses:
# SELECT ... FROM ... JOIN ... ON ... WHERE ... GROUP BY ... HAVING ... ORDER BY ... LIMIT


# ======================= EXERCISES =======================
# Use the employee table above. Write each query, run it with show(...).
# 1. Everyone in Tech earning MORE than 100000.
# 2. Everyone NOT in Sales, sorted by salary, lowest first.
# 3. Everyone whose last name starts with "J".
# 4. The single lowest-paid employee (ORDER BY + LIMIT).
# 5. How many employees, and the total of all salaries.
# 6. The average salary per department, rounded to 2 decimals.
# 7. Departments with more than 2 employees (GROUP BY + HAVING COUNT(*) > 2).


# ======================= PROJECT STEP 13 =======================
# Reports on your bank database (reuse setup_db / save_account / log_txn from step 12,
# copy them into this file).
# Write functions that RETURN the results:
# 1. richest_account(conn)         -> (owner, balance) of the highest balance
# 2. total_money(conn)             -> sum of all balances
# 3. count_by_type(conn)           -> list of (type, count), e.g. [('Checking', 2), ('Savings', 1)]
# 4. big_withdrawals(conn, limit)  -> every withdraw over `limit`, biggest first (use ? for limit)
