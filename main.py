import customtkinter as ctk
import Usecases
import Account
import webbrowser
from PIL import ImageTk, Image
import os

class MainWindow:
    def __init__(self):
        #CREATE WINDOW
        self.window = ctk.CTk()
        self.window.title("League Account Manager")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        self.window.minsize(1300, 200)
        window_width = 1300
        window_height = 1000
        # Get the screen dimension
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        # Find the center point
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        # Set the position of the window to the center of the screen
        self.window.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
        # Window is not resizable
        self.window.resizable(True, True)

        self.u = Usecases.Usecases()
        accounts = self.u.get_all_accounts()
        #print(accounts)
        accounts_frame = ctk.CTkScrollableFrame(self.window, width=window_width,height=int(window_height*0.8),bg_color="transparent", fg_color="transparent")
        accounts_frame.pack(padx=20, pady=20)
        for account in accounts:
            account_frame = ctk.CTkFrame(accounts_frame, bg_color="transparent", fg_color="transparent", border_color="grey", border_width=1)
            
            winrate = round((account.wins / (account.wins+account.losses) * 100),1)
            color = "#42f560"
            if winrate < 50:
                color = "red"

            FONT_SIZE = 20
            FONT = "Arial"
            BUTTON_COLOR = "#3648AC"

            account_Label = ctk.CTkLabel(account_frame, text=f"{account.username}", font=(FONT, FONT_SIZE))
            account_Label.grid(row=0, column=0, pady=10, padx=10)
            account_Label = ctk.CTkLabel(account_frame, text=f"#{account.tag}", font=(FONT, FONT_SIZE))
            account_Label.grid(row=0, column=1, pady=10, padx=10)
            account_Label = ctk.CTkLabel(account_frame, text=account.server, font=(FONT, FONT_SIZE))
            account_Label.grid(row=0, column=2, pady=10, padx=10)
            account_Label = ctk.CTkLabel(account_frame, text=f"{account.division} {account.rank} - {account.lp} LP", font=(FONT, FONT_SIZE))
            account_Label.grid(row=0, column=3, pady=10, padx=10)
            account_Label = ctk.CTkLabel(account_frame, text=f"Wins: {account.wins}", font=(FONT, FONT_SIZE))
            account_Label.grid(row=0, column=4, pady=10, padx=10)
            account_Label = ctk.CTkLabel(account_frame, text=f"Losses: {account.wins}", font=(FONT, FONT_SIZE))
            account_Label.grid(row=0, column=5, pady=10, padx=10)
            account_Label = ctk.CTkLabel(account_frame, text=f"{winrate}%", text_color=color, font=(FONT, FONT_SIZE))
            account_Label.grid(row=0, column=6, pady=10, padx=10)

            login_button = ctk.CTkButton(account_frame, fg_color=BUTTON_COLOR, command=lambda: self.u.login(account.puuid), text="Login", font=(FONT, FONT_SIZE))
            login_button.grid(row=0, column=7, pady=10, padx=10)

            url = "https://op.gg/lol/summoners/euw/" + account.username + "-" + account.tag
            op_gg_button = ctk.CTkButton(account_frame, fg_color=BUTTON_COLOR , command=lambda: webbrowser.open(url, new=0, autoraise=True), text="OPGG", font=(FONT, FONT_SIZE))
            op_gg_button.grid(row=0, column=8, pady=10, padx=10)

            img = Image.open(f"Ranks/{account.division.lower()}.png")
            img = img.resize((40, 40), Image.Resampling.LANCZOS)
            img = ImageTk.PhotoImage(img)
            rank_img = ctk.CTkLabel(account_frame, image=img, text="")
            rank_img.grid(row=0, column=10, pady=10, padx=10)

            account_frame.pack(pady=5)

    def mainloop(self):
        self.window.mainloop()

if __name__ == "__main__":
    app_instance = MainWindow()
    app_instance.mainloop()