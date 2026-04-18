import DatabaseHandler
import Account
import APIHandler
import pyperclip
import pyautogui
import keyboard

class Usecases():
    def __init__(self):
        self.db_handler = DatabaseHandler.DatabaseHandler()
    
    def cpy_u_into_cpy_pw(username : str, password : str):
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

if __name__ == "__main__":
    u = Usecases()
    #accounts = u.get_all_accounts()
    account = u.get_specific_account("Tw5vQtPXXZkiCSwUymQbOeyjf8TdT0zhF5_G9enpd6_nd24aMvo3qxv3xjZdbKn0rjJCFcgd46S7rg")
    print(account)
    #Usecases.cpy_u_into_cpy_pw("EvenTurtle","Hentaisarecool1")