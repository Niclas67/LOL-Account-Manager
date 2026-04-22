import DatabaseHandler
import Account
import pyperclip
import pyautogui
import keyboard
import threading
import time
import os
import subprocess

class Usecases():
    def __init__(self):
        self.db_handler = DatabaseHandler.DatabaseHandler()
        self.api_key = self.db_handler.get_api_key()
    
    def cpy_u_into_cpy_pw(self, username : str, password : str):
        keyboard.wait("space")
        pyperclip.copy(username)
        pyautogui.press("backspace")
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press("tab")
        pyperclip.copy(password)
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press("enter")

    def get_all_accounts(self):
        return self.db_handler.get_all_accounts()

    def get_specific_account(self, puuid):
        return self.db_handler.get_account(puuid)

    def update_specific_account(self, puuid):
        account = self.db_handler.get_account(puuid)
        account.update_info()
        self.db_handler.update_account(account)
        return account


    def update_all_accounts(self):
        accounts = self.get_all_accounts()
        output = []
        for account in accounts:
            account.update_info()
            self.db_handler.update_account(account)
            output.append(account)
            print("done")
        return output

    
    def update_password(self, puuid : str, new_password : str):
        account = self.db_handler.get_account(puuid)
        account.update_password(new_password)
        self.db_handler.update_account(account)
        return account

    def update_email(self, puuid : str, new_email: str):
        account = self.db_handler.get_account(puuid)
        account.email = new_email
        self.db_handler.update_account(account)
        return account

    def update_server(self, puuid : str, new_server: str):
        account = self.db_handler.get_account(puuid)
        account.server = new_server
        self.db_handler.update_account(account)
        return account

    def get_login_credentials(self, puuid : str):
        return self.db_handler.get_account(puuid).get_login_credentials()

    def login(self, puuid : str):
        login_credentials = self.get_login_credentials(puuid)
        def worker():
            self.cpy_u_into_cpy_pw(*login_credentials)
        t = threading.Thread(target=worker, daemon=True)
        t.start()


    def register_new_account(self, username : str, tag : str, login_username : str, password : str, server="EUW", email=""):
        account = Account.register_new_account(username, tag, login_username, password, server, email)
        self.db_handler.add_account(account)
        return account

    def remove_account(self, puuid : str):
            self.db_handler.delete_account(puuid)

    
def close_league():
    to_kill = ["RiotClientServices.exe","RiotClientCrashHandler.exe","LeagueClient.exe","LeagueCrashHandler64.exe","LeagueClientUx.exe","LeagueClientUxRender.exe"]
    for entry in to_kill:
        try:
            os.system("taskkill /F /im " + entry)
        except:
            pass
        
def launch_league():
    riot_client_path = r"C:\Riot Games\Riot Client\RiotClientServices.exe"
    launch_arguments = [
        "--launch-product=league_of_legends",
        "--launch-patchline=live"
    ]
    subprocess.run([riot_client_path] + launch_arguments)

def fix_league():
    def worker():
        close_league()
        launch_league()
    t = threading.Thread(target=worker, daemon=True)
    t.start()

if __name__ == "__main__":
    u = Usecases()
    #u.register_new_account("Lexie Liu", "vbuck", "eventurtle", "Hentaisarecool1")
    u.login("dlksAYa2w6I-W3NscGQatfT89_BHRBH3HnKjpLuzM8itf6fa2tpBsOUKxfhZxEgA-lsmL7WpqbrONQ")
    print("HERE")
    for i in range(10):
        print(i)
        time.sleep(1)
