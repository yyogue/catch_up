# 14: SQL joins
# Run: python3 14_sql_joins.py

import sqlite3

# ======================= SETUP =======================
conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.executescript("""
    CREATE TABLE location (id INTEGER PRIMARY KEY AUTOINCREMENT, city TEXT);
    INSERT INTO location (city) VALUES ('Reston'), ('Arlington'), ('Los Angeles'), ('Houston');

    CREATE TABLE employee (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT, salary REAL,
        location_id INTEGER REFERENCES location(id)
    );
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


# ======================= EXAMPLES =======================
# employee.location_id is a FOREIGN KEY pointing to location.id.
# Write table.column when both tables have a column with the same name (like id).

# ---- INNER JOIN: only rows that match on BOTH sides ----
show("""SELECT employee.name, location.city
        FROM employee
        INNER JOIN location ON employee.location_id = location.id;""")      # Nadia (NULL) is missing

# ---- JOIN + WHERE (the Revature question) ----
show("""SELECT employee.name, employee.salary
        FROM employee
        INNER JOIN location ON employee.location_id = location.id
        WHERE location.city = 'Reston' AND employee.salary > 100000;""")

# ---- JOIN + WHERE + ORDER BY (the other Revature question) ----
show("""SELECT employee.name, employee.salary
        FROM employee
        INNER JOIN location ON employee.location_id = location.id
        WHERE location.city = 'Arlington'
        ORDER BY employee.salary ASC;""")

# ---- LEFT JOIN: EVERY row from the left table, None where there's no match ----
show("""SELECT employee.name, location.city
        FROM employee
        LEFT JOIN location ON employee.location_id = location.id;""")      # Nadia shows with None

# ---- Find what's missing: LEFT JOIN + IS NULL ----
show("""SELECT location.city
        FROM location
        LEFT JOIN employee ON location.id = employee.location_id
        WHERE employee.id IS NULL;""")                                    # Houston: no employees

# ---- JOIN on a text column ----
show("""SELECT student.id, student.student_name
        FROM student
        INNER JOIN class ON student.class_title = class.class_title
        WHERE class.teacher_name = 'Ms. Lovelace';""")

show("""SELECT class.class_title, student.student_name
        FROM class
        LEFT JOIN student ON class.class_title = student.class_title;""")  # Biology has no students

# ---- RIGHT JOIN = LEFT JOIN with the tables swapped (SQLite 3.39+ supports RIGHT JOIN) ----
show("""SELECT class.teacher_name, student.student_name
        FROM student
        LEFT JOIN class ON student.class_title = class.class_title;""")    # Jessica (Art) has no teacher

# ---- JOIN + GROUP BY ----
show("""SELECT location.city, COUNT(employee.id) AS people, ROUND(AVG(employee.salary), 2) AS avg_pay
        FROM location
        LEFT JOIN employee ON location.id = employee.location_id
        GROUP BY location.city
        ORDER BY people DESC;""")

# ---- Short names with aliases ----
show("""SELECT e.name, l.city
        FROM employee AS e
        JOIN location AS l ON e.location_id = l.id;""")                  # JOIN alone = INNER JOIN


# ======================= EXERCISES =======================
# Use the tables above.
# 1. Every employee's name and city, sorted by city.
# 2. Employees in Los Angeles earning more than 100000.
# 3. Every employee, with "None" for city when they have no location (LEFT JOIN).
# 4. Every class and how many students it has, including classes with 0 students.
# 5. Every student whose class has no teacher (LEFT JOIN + IS NULL).
# 6. The city with the highest average salary (JOIN + GROUP BY + ORDER BY + LIMIT 1).


# ======================= PROJECT STEP 14 =======================
# Reports that need BOTH bank tables (copy setup_db etc. from step 12):
# 1. statement(conn, account_id) -> every transaction for that account WITH the owner's name:
#       ('Youssouf', 'deposit', 200.0), ...
# 2. txn_summary(conn) -> for EVERY account (even with no transactions):
#       owner, number of transactions, total amount   (LEFT JOIN + GROUP BY)
# 3. inactive_accounts(conn) -> owners with no transactions at all (LEFT JOIN + IS NULL)
