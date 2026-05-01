import sqlite3
from Account import Account, register_new_account

class DatabaseHandler():
    def __init__(self):
        self.con = sqlite3.connect("Accounts.db")
        self.cur = self.con.cursor()
    
    def create_api_key_table(self):
        self.cur.execute("""
                        CREATE TABLE api_key(
                        key TEXT
                        )
                        """)
    def add_api_key(self, api_key : str):
        self.cur.execute("""
                        INSERT INTO api_key VALUES (?)
                         """, (api_key,))
        self.con.commit()
    
    def update_api_key(self, api_key : str):
        self.cur.execute("""
                        DELETE FROM api_key
                        """)
        self.con.commit()
        self.add_api_key(api_key)

    def get_api_key(self):
        self.cur.execute("""
                        SELECT key FROM api_key
                         """)
        return self.cur.fetchall()[0][0]

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
        o = o.fetchall()
        if len(o)<1:
            return None
        accounts = []
        for account in o:
            accounts.append(Account(*account))
        return accounts
            

if __name__ == "__main__":
    db_handler = DatabaseHandler()
    db_handler.create_table()
    db_handler.create_api_key_table()