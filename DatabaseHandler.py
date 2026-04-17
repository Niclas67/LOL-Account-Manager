import sqlite3
from Account import Account
import APIHandler

class DatabaseHandler():
    def __init__(self):
        self.con = sqlite3.connect("lol_account_manager/Accounts.db")
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

    def update_info(self, puuid : str):
        info = APIHandler.get_summonerInfo(puuid)
        self.cur.execute("""
                        Update accounts
                        SET division = ?,
                            rank = ?,
                            lp = ?,
                            wins = ?,
                            losses = ?
                        WHERE puuid = ?
                         """, (info['division'], info['rank'], info['lp'], info['wins'], info['losses'], puuid))
        self.con.commit()


if __name__ == "__main__":
    DatabaseHandler().update_info("g-o7F9BEm8tdLMrb5-dKiPHgODbCO0SEgIDU6N9PoS8zj0nWEVJ6rk4GiTPtyXIBoY0amH3udNRdwQ")
    #db_handler = DatabaseHandler()
    #db_handler.update_username("g-o7F9BEm8tdLMrb5-dKiPHgODbCO0SEgIDU6N9PoS8zj0nWEVJ6rk4GiTPtyXIBoY0amH3udNRdwQ", "new_username")
    #db_handler.add_account(Account("ballsohard", "EUW", "login_username", "password"))

    
