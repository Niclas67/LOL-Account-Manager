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

if __name__ == "__main__":
    u = Usecases()
    accounts = u.get_all_accounts()
    for account in accounts:
        print(account)
    #Usecases.cpy_u_into_cpy_pw("EvenTurtle","Hentaisarecool1")