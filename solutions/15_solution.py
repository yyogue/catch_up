# Solution for 15_final_project.py: the full mini bank app
import sqlite3
from abc import ABC, abstractmethod


# ======================= 1. ERRORS =======================
class InsufficientFundsError(Exception):
    pass


class InvalidAmountError(Exception):
    pass


# ======================= 2. HELPERS =======================
def mask_account(number):
    return "****" + number[-4:]


def format_owner(name):
    return name.strip().title()


# ======================= 3. CLASSES =======================
class Account(ABC):
    def __init__(self, owner, number, balance=0):
        self.owner = format_owner(owner)
        self.number = number
        self._balance = balance
        self.history = []
        self.db_id = None

    @abstractmethod
    def account_type(self):
        pass

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError(f"Deposit must be more than 0, got {amount}")
        self._balance += amount
        self.history.append(("deposit", amount))

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError(f"Withdraw must be more than 0, got {amount}")
        if amount > self._balance:
            raise InsufficientFundsError(f"Only ${self._balance:.2f} available")
        self._balance -= amount
        self.history.append(("withdraw", amount))

    def get_balance(self):
        return self._balance

    def __str__(self):
        return f"{self.account_type():8} | {self.owner:14} | {mask_account(self.number)} | ${self._balance:.2f}"


class Checking(Account):
    FEE = 1

    def account_type(self):
        return "Checking"

    def withdraw(self, amount):
        super().withdraw(amount + self.FEE)


class Savings(Account):
    def __init__(self, owner, number, balance=0, rate=0.02):
        super().__init__(owner, number, balance)
        self.rate = rate

    def account_type(self):
        return "Savings"

    def add_interest(self):
        self.deposit(round(self._balance * self.rate, 2))


# ======================= 4. DATABASE =======================
def setup_db(path=":memory:"):
    conn = sqlite3.connect(path)
    conn.execute("PRAGMA foreign_keys = ON;")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS account (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            owner TEXT, account_number TEXT, type TEXT, balance REAL
        );
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS txn (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            account_id INTEGER REFERENCES account(id),
            kind TEXT, amount REAL
        );
    """)
    conn.commit()
    return conn


def save_account(conn, acct):
    cur = conn.execute(
        "INSERT INTO account (owner, account_number, type, balance) VALUES (?, ?, ?, ?);",
        (acct.owner, acct.number, acct.account_type(), acct.get_balance()),
    )
    conn.commit()
    acct.db_id = cur.lastrowid
    return acct.db_id


def record(conn, acct, kind, amount):
    conn.execute("INSERT INTO txn (account_id, kind, amount) VALUES (?, ?, ?);", (acct.db_id, kind, amount))
    conn.execute("UPDATE account SET balance = ? WHERE id = ?;", (acct.get_balance(), acct.db_id))
    conn.commit()


def total_money(conn):
    return conn.execute("SELECT SUM(balance) FROM account;").fetchone()[0]


def txn_summary(conn):
    return conn.execute("""
        SELECT account.owner, COUNT(txn.id), SUM(txn.amount)
        FROM account
        LEFT JOIN txn ON account.id = txn.account_id
        GROUP BY account.id
        ORDER BY account.owner;
    """).fetchall()


def biggest_txns(conn, limit=3):
    return conn.execute("""
        SELECT account.owner, txn.kind, txn.amount
        FROM txn
        INNER JOIN account ON txn.account_id = account.id
        ORDER BY txn.amount DESC
        LIMIT ?;
    """, (limit,)).fetchall()


# ======================= 5. FILES =======================
def write_statement(acct, filename):
    with open(filename, "w") as f:
        f.write(f"Statement: {acct.owner} ({acct.account_type()} {mask_account(acct.number)})\n")
        for kind, amount in acct.history:
            f.write(f"  {kind:9} ${amount:.2f}\n")
        f.write(f"Balance: ${acct.get_balance():.2f}\n")


# ======================= 6. PROGRAM =======================
def process(conn, acct, kind, amount):
    try:
        if kind == "deposit":
            acct.deposit(amount)
        else:
            acct.withdraw(amount)
        record(conn, acct, kind, acct.history[-1][1])   # history has the real amount (fee included)
        print(f"OK    {acct.owner:14} {kind:8} ${amount}")
        return True
    except (InsufficientFundsError, InvalidAmountError) as e:
        print(f"FAIL  {acct.owner:14} {kind:8} ${amount}: {e}")
        return False


def main():
    conn = setup_db()
    accounts = [
        Checking("  youssouf YOGUE ", "ACC-48213907", 500),
        Savings("amina diallo", "ACC-55102266", 1000, rate=0.05),
        Checking("ben carter", "ACC-77310045", 50),
    ]
    for acct in accounts:
        save_account(conn, acct)

    actions = [
        (0, "deposit", 200), (1, "withdraw", 150), (2, "withdraw", 80),
        (0, "withdraw", 99), (1, "deposit", -20), (2, "deposit", 300),
    ]
    print("--- Processing ---")
    for index, kind, amount in actions:
        process(conn, accounts[index], kind, amount)

    for acct in accounts:
        if isinstance(acct, Savings):
            acct.add_interest()
            record(conn, acct, "interest", acct.history[-1][1])

    print("\n--- Accounts, richest first ---")
    for acct in sorted(accounts, key=lambda a: a.get_balance(), reverse=True):
        print(acct)

    print(f"\nTotal money in the bank: ${total_money(conn):.2f}")

    print("\n--- Transactions per owner ---")
    for owner, count, total in txn_summary(conn):
        print(f"{owner}: {count} transaction(s), ${total or 0:.2f}")

    print("\n--- Biggest transactions ---")
    for owner, kind, amount in biggest_txns(conn):
        print(f"{owner:15} {kind:9} ${amount:.2f}")

    write_statement(accounts[0], "statement.txt")
    with open("statement.txt") as f:
        print("\n--- statement.txt ---")
        print(f.read())

    conn.close()


if __name__ == "__main__":
    main()
