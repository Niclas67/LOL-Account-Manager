import DatabaseHandler
import Account
import APIHandler
import pyperclip
import pyautogui
import keyboard

class Usecases():
    def __init__(self):
        self.db_handler = DatabaseHandler.DatabaseHandler()
    
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
        self.cpy_u_into_cpy_pw(*self.get_login_credentials(puuid))
    
    def register_new_account(self, username : str, tag : str, login_username : str, password : str, server="EUW", email=""):
        account = Account.register_new_account(username, tag, login_username, password, server, email)
        self.db_handler.add_account(account)
        return account

    def remove_account(self, puuid : str):
        self.db_handler.delete_account(puuid)

if __name__ == "__main__":
    u = Usecases()
    #u.register_new_account("Lexie Liu", "vbuck", "eventurtle", "Hentaisarecool1")
    u.login("dlksAYa2w6I-W3NscGQatfT89_BHRBH3HnKjpLuzM8itf6fa2tpBsOUKxfhZxEgA-lsmL7WpqbrONQ")
    #account = u.get_specific_account("Tw5vQtPXXZkiCSwUymQbOeyjf8TdT0zhF5_G9enpd6_nd24aMvo3qxv3xjZdbKn0rjJCFcgd46S7rg")
    #print(account.get_login_credentials())
    #Usecases.cpy_u_into_cpy_pw("EvenTurtle","Hentaisarecool1")