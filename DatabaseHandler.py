import sqlite3
from Account import Account, register_new_account
import APIHandler

class DatabaseHandler():
    def __init__(self):
        self.con = sqlite3.connect("Accounts.db")
        self.cur = self.con.cursor()

    def create_table(self):
        self.cur.execute("""
                         CREATE TABLE accounts(
                         username TEXT,
                         tag TEXT,
                         login_username TEXT,
                         password TEXT,
                         server TEXT,
                         email TEXT,
                         puuid TEXT,
                         division TEXT,
                         rank TEXT,
                         lp INTEGER,
                         wins INTEGER,
                         losses INTEGER
                         )
                         """)

    def add_account(self, new_account : Account):
        self.cur.execute("""
        INSERT INTO accounts VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            new_account.username,
            new_account.tag,
            new_account.login_username,
            new_account.password,
            new_account.server,
            new_account.email,
            new_account.puuid,
            new_account.division,
            new_account.rank,
            new_account.lp,
            new_account.wins,
            new_account.losses
        ))
        self.con.commit()

    def update_username(self, puuid : str, new_username : str):
        self.cur.execute("""
                        UPDATE accounts
                        SET username = ?,
                        WHERE puuid = ?
                         """, (new_username, puuid))
        self.con.commit()

    def update_account(self, account : Account):
        self.cur.execute("""
                        UPDATE accounts
                        SET username = ?,
                            tag = ?,
                            login_username = ?,
                            password = ?,
                            server = ?,
                            email = ?,
                            division = ?,
                            rank = ?,
                            lp = ?,
                            wins = ?,
                            losses = ?
                        WHERE puuid = ?
                        """, (account.username,account.tag,account.login_username,account.password,account.server,account.email,account.division,account.rank,account.lp,account.wins,account.losses,account.puuid))
        self.con.commit()

    def get_account(self, puuid : str):
        o = self.cur.execute("""
                        SELECT *
                        FROM accounts
                        WHERE puuid = ?
                        """, (puuid,))
        return Account(*o.fetchone())

    def delete_account(self, puuid : str):
        self.cur.execute("""
                        DELETE 
                        FROM accounts
                        WHERE puuid = ? 
                        """, (puuid,))
        self.con.commit()

    def get_all_accounts(self):
        o = self.cur.execute("SELECT * FROM accounts")
        return o.fetchall()

if __name__ == "__main__":
    db_handler = DatabaseHandler()
    print(db_handler.get_all_accounts())
    #account = register_new_account("Masaru","445","tlun","t_pw")
    #db_handler.add_account(account)
    #db_handler.delete_account("g-o7F9BEm8tdLMrb5-dKiPHgODbCO0SEgIDU6N9PoS8zj0nWEVJ6rk4GiTPtyXIBoY0amH3udNRdwQ")
    #account = db_handler.get_account("JcGQa-Q3kLBp6leFDw44QwqKpXFJzrd0v8-BVq6FbUR6f8RbM2yvfJTBxEstuaw5Gw7fj9GrVMJfaQ")
    #account.username = "TEST"
    #account.update_info()
    #db_handler.update_account(account)
    #print(account)