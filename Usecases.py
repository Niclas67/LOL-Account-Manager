import DatabaseHandler
import Account
import APIHandler
import pyperclip
import pyautogui
import keyboard

class Usecases():
    def __init__(self):
        self.db_handler = DatabaseHandler.DatabaseHandler()
    
    def cpy_u_into_cp_pw(username : str, password : str):
        print("Press SPACE to fill in credentials...")
        keyboard.wait("space")

        pyperclip.copy(username)
        pyautogui.press("backspace")
        pyautogui.hotkey("ctrl", "v")

        pyautogui.press("tab")

        pyperclip.copy(password)
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press("enter")

if __name__ == "__main__":
    Usecases.cpy_u_into_cp_pw("EvenTurtle","Hentaisarecool1")