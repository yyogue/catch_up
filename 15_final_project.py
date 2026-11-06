# 15: FINAL PROJECT: the mini bank app
# Run: python3 15_final_project.py
#
# You built every piece in steps 1 to 14. Now put them together in ONE program.
# Copy your own code from earlier steps where you can. Fill every TODO.
# When it's done, uncomment main() at the bottom and run it.
#
# What the finished app does:
#   - Account classes with inheritance (Checking with a fee, Savings with interest)
#   - Custom errors for bad amounts and not enough money
#   - Every account and transaction saved in a SQLite database
#   - Reports with SQL (aggregates, GROUP BY, JOINs)
#   - A text statement written to a file
#   - A small menu loop so you can use it from the terminal

import sqlite3
from abc import ABC, abstractmethod


# ======================= 1. ERRORS (step 8) =======================
# TODO: InsufficientFundsError and InvalidAmountError, both from Exception


# ======================= 2. HELPERS (steps 2 and 7) =======================
def mask_account(number):
    """'ACC-48213907' -> '****3907'"""
    # TODO
    pass


def format_owner(name):
    """'  youssouf YOGUE ' -> 'Youssouf Yogue'"""
    # TODO
    pass


# ======================= 3. CLASSES (steps 9 and 10) =======================
class Account(ABC):
    def __init__(self, owner, number, balance=0):
        # TODO: owner (use format_owner), number, _balance, history = [], db_id = None
        pass

    @abstractmethod
    def account_type(self):
        pass

    def deposit(self, amount):
        # TODO: raise InvalidAmountError if amount <= 0, add it, append to history
        pass

    def withdraw(self, amount):
        # TODO: raise InvalidAmountError if amount <= 0,
        #       raise InsufficientFundsError if amount > balance,
        #       subtract it, append to history
        pass

    def get_balance(self):
        # TODO
        pass

    def __str__(self):
        # TODO: "Checking | Youssouf Yogue | ****3907 | $1250.50"
        pass


class Checking(Account):
    FEE = 1

    def account_type(self):
        return "Checking"

    def withdraw(self, amount):
        # TODO: withdraw amount + FEE using super()
        pass


class Savings(Account):
    def __init__(self, owner, number, balance=0, rate=0.02):
        # TODO: super().__init__ then self.rate
        pass

    def account_type(self):
        return "Savings"

    def add_interest(self):
        # TODO: add balance * rate (round to 2 decimals) as a deposit
        pass


# ======================= 4. DATABASE (steps 12 to 14) =======================
def setup_db(path=":memory:"):
    # TODO: connect, foreign keys ON, CREATE TABLE IF NOT EXISTS account and txn, return conn
    pass


def save_account(conn, acct):
    # TODO: INSERT the account, store cur.lastrowid in acct.db_id, return it
    pass


def record(conn, acct, kind, amount):
    # TODO: INSERT into txn AND UPDATE the account balance, then commit
    pass


def total_money(conn):
    # TODO: SUM of all balances
    pass


def txn_summary(conn):
    # TODO: owner, number of transactions, total amount, for EVERY account (LEFT JOIN + GROUP BY)
    pass


def biggest_txns(conn, limit=3):
    # TODO: owner, kind, amount, biggest first, LIMIT ?
    pass


# ======================= 5. FILES (step 11) =======================
def write_statement(acct, filename):
    # TODO: header line, one line per transaction in acct.history, final balance
    pass


# ======================= 6. PROGRAM (steps 6 and 8) =======================
def process(conn, acct, kind, amount):
    """Runs one action safely. Returns True if it worked."""
    # TODO: try deposit/withdraw, record it in the db (use acct.history[-1][1] so the
    #       Checking fee is included), print OK
    #       except your 2 errors: print FAIL with the message, return False
    pass


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

    # BONUS: a menu loop
    # while True:
    #     choice = input("\n1) balance  2) deposit  3) withdraw  q) quit: ")
    #     if choice == "q":
    #         break
    #     ...

    conn.close()


# Uncomment when every TODO is done:
# if __name__ == "__main__":
#     main()
print("Fill in the TODOs, then uncomment main() at the bottom of this file.")
