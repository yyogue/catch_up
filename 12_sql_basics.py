# 12: SQL basics with sqlite3
# Run: python3 12_sql_basics.py

import sqlite3

# ======================= EXAMPLES =======================

def show(cur, sql):
    """Small helper: runs a SELECT and prints the rows."""
    print(">", sql)
    for row in cur.execute(sql).fetchall():
        print("  ", row)

# ---- 1. Connect ----
conn = sqlite3.connect(":memory:")    # RAM only. Use "app.db" for a real file.
cur = conn.cursor()                   # the cursor runs the SQL

# ---- 2. CREATE TABLE (DDL) ----
cur.execute("""
    CREATE TABLE IF NOT EXISTS song (
        id INTEGER PRIMARY KEY AUTOINCREMENT,   -- unique, auto-numbered
        title varchar(100),
        artist varchar(100)
    );
""")

# ---- 3. INSERT (DML) ----
cur.execute("INSERT INTO song (title, artist) VALUES ('Let it be', 'Beatles');")

# ALWAYS use ? placeholders for values from variables (stops SQL injection,
# and names like O'Malley don't break the query)
title, artist = "Hotel California", "Eagles"
cur.execute("INSERT INTO song (title, artist) VALUES (?, ?);", (title, artist))

# insert many at once
songs = [("Kashmir", "Led Zeppelin"), ("Africa", "Toto"), ("Don't Stop", "Fleetwood Mac")]
cur.executemany("INSERT INTO song (title, artist) VALUES (?, ?);", songs)
conn.commit()                         # save changes
print("last id:", cur.lastrowid)

# ---- 4. SELECT (DQL) ----
show(cur, "SELECT * FROM song;")
show(cur, "SELECT title FROM song;")

cur.execute("SELECT * FROM song WHERE id = ?;", (2,))
print("fetchone:", cur.fetchone())    # one row as a tuple

for song_id, t, a in cur.execute("SELECT * FROM song;"):   # unpack each row
    print(f"{song_id}. {t} by {a}")

# ---- 5. UPDATE (always with WHERE) ----
cur.execute("UPDATE song SET artist = ? WHERE title = ?;", ("The Beatles", "Let it be"))
print("rows changed:", cur.rowcount)

# ---- 6. DELETE (always with WHERE) ----
cur.execute("DELETE FROM song WHERE id = ?;", (4,))
conn.commit()
show(cur, "SELECT * FROM song;")

# ---- 7. ALTER: add a column ----
cur.execute("ALTER TABLE song ADD year int;")
cur.execute("UPDATE song SET year = 1977 WHERE title = 'Hotel California';")
show(cur, "SELECT * FROM song;")      # other rows get None (NULL)

# ---- 8. VIEW: a saved SELECT with a name ----
cur.execute("CREATE VIEW song_titles AS SELECT title, artist FROM song;")
show(cur, "SELECT * FROM song_titles;")

# ---- 9. Foreign key ----
cur.execute("PRAGMA foreign_keys = ON;")    # SQLite has them off by default
cur.execute("""
    CREATE TABLE play (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        song_id int REFERENCES song(id),
        played_on TEXT
    );
""")
cur.execute("INSERT INTO play (song_id, played_on) VALUES (1, '2026-10-18');")
try:
    cur.execute("INSERT INTO play (song_id, played_on) VALUES (99, '2026-10-18');")
except sqlite3.IntegrityError as e:
    print("Blocked:", e)              # song 99 doesn't exist

# ---- 10. DROP: delete the whole table ----
cur.execute("DROP VIEW song_titles;")
cur.execute("CREATE TABLE temp_table (x int);")
cur.execute("DROP TABLE temp_table;")
show(cur, "SELECT name FROM sqlite_master WHERE type = 'table';")

conn.close()

# Statement types:
#   DDL (structure): CREATE, ALTER, DROP
#   DML (data):      INSERT, UPDATE, DELETE
#   DQL (reading):   SELECT


# ======================= EXERCISES =======================
# Use a fresh connection: conn = sqlite3.connect(":memory:")
# 1. Create a table dogs (id auto-increment primary key, name, breed, age int).

# 2. Write insert_dog(cur, name, breed, age) using ? placeholders. Insert 3 dogs,
#    one of them named "O'Malley".

# 3. Write select_all_dogs(cur) that RETURNS all rows. Print them.

# 4. Update one dog's age. Delete another dog. Print the table again.

# 5. Add a column "owner" with ALTER TABLE. Set it for one dog.

# 6. Create a view dog_names with only the name and breed columns. Select from it.


# ======================= PROJECT STEP 12 =======================
# Move the bank into a database.
# 1. Write setup_db() that connects to ":memory:" and creates 2 tables:
#      account: id (PK autoincrement), owner TEXT, account_number TEXT, type TEXT, balance REAL
#      txn:     id (PK autoincrement), account_id int REFERENCES account(id), kind TEXT, amount REAL
#    Return the connection.
# 2. save_account(conn, owner, number, type, balance) -> inserts with ?, returns cur.lastrowid
# 3. log_txn(conn, account_id, kind, amount) -> inserts a transaction
# 4. update_balance(conn, account_id, new_balance) -> UPDATE with WHERE id = ?
# 5. Create 3 accounts, log a few transactions, then print both tables.
