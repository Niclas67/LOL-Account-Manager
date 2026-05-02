import customtkinter as ctk
import libraries.Usecases as Usecases
import libraries.Account as Account
import webbrowser

from libraries.DatabaseHandler import DatabaseHandler
from libraries.Usecases import close_league, fix_league, launch_league
from PIL import ImageTk, Image
import os
import ctypes

FONT_SIZE = 20
FONT = "Arial"
BUTTON_COLOR = "#3648AC"
PAD_X = 0
REAL_PAD_X = 20

class MainWindow:
    def __init__(self):
        #CREATE WINDOW
        global window
        window = ctk.CTk()
        self.window = window
        self.window.title("League Account Manager")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        window.iconbitmap("cherry.ico")
        myappid = "mycompany.myapp.uniqueid"
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        self.window.minsize(1300, 200)
        window_width = 1300
        window_height = 700
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

        top_frame = ctk.CTkFrame(self.window, bg_color="transparent", fg_color="transparent")
        top_frame.pack()

        add_account_button = ctk.CTkButton(top_frame, width=50, fg_color=BUTTON_COLOR , command=lambda: self.add_account_window(self.window), text="Add Account", font=(FONT, FONT_SIZE))
        add_account_button.grid(row=0, column=0, padx=20, pady=20)


        def update_all_and_restart():
            self.u.update_all_accounts()
            window.destroy()
            app_instance = MainWindow()
            app_instance.mainloop()

        update_all_button = ctk.CTkButton(top_frame, width=50, fg_color=BUTTON_COLOR , command=lambda: update_all_and_restart(), text="Update all Accounts", font=(FONT, FONT_SIZE))
        update_all_button.grid(row=0, column=1, padx=20, pady=20)

        close_lol_button = ctk.CTkButton(top_frame, width=50, fg_color=BUTTON_COLOR , command=lambda: close_league(), text="Close League", font=(FONT, FONT_SIZE))
        close_lol_button.grid(row=0, column=2, padx=20, pady=20)

        restart_lol_button = ctk.CTkButton(top_frame, width=50, fg_color=BUTTON_COLOR , command=lambda: fix_league(), text="Restart League", font=(FONT, FONT_SIZE))
        restart_lol_button.grid(row=0, column=3, padx=20, pady=20)

        enter_api_key_button = ctk.CTkButton(top_frame, width=50, fg_color=BUTTON_COLOR , command=lambda: self.api_window(self.window), text="Enter API-Key", font=(FONT, FONT_SIZE))
        enter_api_key_button.grid(row=0, column=4, padx=20, pady=20)


        accounts_frame = ctk.CTkScrollableFrame(self.window, width=window_width,height=int(window_height*0.8),bg_color="transparent", fg_color="transparent")
        accounts_frame.pack(padx=20, pady=20)

        



        if not accounts:
            return
        for i, account in enumerate(accounts):
            row = i * 2
            if (account.wins == "0" and account.losses == "0") or "/" in (account.wins, account.losses):
                winrate = 0.0
            else:
                winrate = round((int(account.wins) / (int(account.wins) + int(account.losses)) * 100),1)
            color = "#42f560"
            if winrate < 50:
                color = "red"

            account_Label = ctk.CTkLabel(accounts_frame, text=f"{account.username}", font=(FONT, FONT_SIZE))
            account_Label.grid(row=row, column=0, pady=10, padx=PAD_X)
            self.window.update_idletasks()
            width = account_Label.winfo_width()+REAL_PAD_X
            separator = ctk.CTkFrame(accounts_frame, height=2, fg_color="#575260", width=width)
            separator.grid(row=row + 1, column=0, sticky="ew", padx=PAD_X)

            account_Label = ctk.CTkLabel(accounts_frame, text=f"#{account.tag}", font=(FONT, FONT_SIZE))
            account_Label.grid(row=row, column=1, pady=10, padx=PAD_X)
            self.window.update_idletasks()
            width = account_Label.winfo_width()+REAL_PAD_X
            separator = ctk.CTkFrame(accounts_frame, height=2, fg_color="#575260", width=width)
            separator.grid(row=row + 1, column=1, sticky="ew", padx=PAD_X)

            account_Label = ctk.CTkLabel(accounts_frame, text=account.server, font=(FONT, FONT_SIZE))
            account_Label.grid(row=row, column=2, pady=10, padx=PAD_X)
            self.window.update_idletasks()
            width = account_Label.winfo_width()+REAL_PAD_X
            separator = ctk.CTkFrame(accounts_frame, height=2, fg_color="#575260", width=width)
            separator.grid(row=row + 1, column=2, sticky="ew", padx=PAD_X)

            img = Image.open(f"Ranks/{account.division.lower()}.png")
            img = img.resize((40, 40), Image.Resampling.LANCZOS)
            img = ImageTk.PhotoImage(img)
            rank_img = ctk.CTkLabel(accounts_frame, image=img, text="")
            rank_img.grid(row=row, column=3, pady=10, padx=PAD_X)
            self.window.update_idletasks()
            width = rank_img.winfo_width()+REAL_PAD_X
            separator = ctk.CTkFrame(accounts_frame, height=2, fg_color="#575260", width=width)
            separator.grid(row=row + 1, column=3, sticky="ew", padx=PAD_X)

            account_Label = ctk.CTkLabel(accounts_frame, text=f"{account.division} {account.rank} - {account.lp} LP", font=(FONT, FONT_SIZE))
            account_Label.grid(row=row, column=4, pady=10, padx=PAD_X)
            self.window.update_idletasks()
            width = account_Label.winfo_width()+REAL_PAD_X
            separator = ctk.CTkFrame(accounts_frame, height=2, fg_color="#575260", width=width)
            separator.grid(row=row + 1, column=4, sticky="ew", padx=PAD_X)

            account_Label = ctk.CTkLabel(accounts_frame, text=f"Wins: {account.wins}", font=(FONT, FONT_SIZE))
            account_Label.grid(row=row, column=5, pady=10, padx=PAD_X)
            self.window.update_idletasks()
            width = account_Label.winfo_width()+REAL_PAD_X
            separator = ctk.CTkFrame(accounts_frame, height=2, fg_color="#575260", width=width)
            separator.grid(row=row + 1, column=5, sticky="ew", padx=PAD_X)

            account_Label = ctk.CTkLabel(accounts_frame, text=f"Losses: {account.losses}", font=(FONT, FONT_SIZE))
            account_Label.grid(row=row, column=6, pady=10, padx=PAD_X)
            self.window.update_idletasks()
            width = account_Label.winfo_width()+REAL_PAD_X
            separator = ctk.CTkFrame(accounts_frame, height=2, fg_color="#575260", width=width)
            separator.grid(row=row + 1, column=6, sticky="ew", padx=PAD_X)

            account_Label = ctk.CTkLabel(accounts_frame, text=f"{winrate}%", text_color=color, font=(FONT, FONT_SIZE))
            account_Label.grid(row=row, column=7, pady=10, padx=PAD_X)
            self.window.update_idletasks()
            width = account_Label.winfo_width()+REAL_PAD_X
            separator = ctk.CTkFrame(accounts_frame, height=2, fg_color="#575260", width=width)
            separator.grid(row=row + 1, column=7, sticky="ew", padx=PAD_X)

            puuid = account.puuid
            login_button = ctk.CTkButton(accounts_frame, fg_color=BUTTON_COLOR, command=lambda puuid=puuid: self.u.login(puuid), text="Login", font=(FONT, FONT_SIZE))
            login_button.grid(row=row, column=8, pady=10, padx=PAD_X)
            self.window.update_idletasks()
            width = login_button.winfo_width()+REAL_PAD_X
            separator = ctk.CTkFrame(accounts_frame, height=2, fg_color="#575260", width=width)
            separator.grid(row=row + 1, column=8, sticky="ew", padx=PAD_X)

            url = "https://op.gg/lol/summoners/euw/" + account.username + "-" + account.tag
            op_gg_button = ctk.CTkButton(accounts_frame, width=50, fg_color=BUTTON_COLOR , command=lambda url=url: webbrowser.open(url, new=0, autoraise=True), text="OPGG", font=(FONT, FONT_SIZE))
            op_gg_button.grid(row=row, column=9, pady=10, padx=PAD_X)
            self.window.update_idletasks()
            width = op_gg_button.winfo_width()+REAL_PAD_X
            separator = ctk.CTkFrame(accounts_frame, height=2, fg_color="#575260", width=width)
            separator.grid(row=row + 1, column=9, sticky="ew", padx=PAD_X)

            update_button = ctk.CTkButton(accounts_frame, width=50, fg_color=BUTTON_COLOR , command=lambda puuid=puuid: self.update_window(self.window, puuid), text="Update", font=(FONT, FONT_SIZE))
            update_button.grid(row=row, column=10, pady=10, padx=PAD_X)
            self.window.update_idletasks()
            width = op_gg_button.winfo_width()+REAL_PAD_X
            separator = ctk.CTkFrame(accounts_frame, height=2, fg_color="#575260", width=width)
            separator.grid(row=row + 1, column=10, sticky="ew", padx=PAD_X)
            
    class update_window():
        def __init__(self, window, puuid):
            self.toplevel = ctk.CTkToplevel(window)
            self.toplevel.title("Update Account")
            self.toplevel.transient(window)
            self.toplevel.lift()
            self.toplevel.focus_force() 
            ctk.set_appearance_mode("dark")
            ctk.set_default_color_theme("blue")
            self.toplevel.minsize(800, 600)
            window_width = 800
            window_height = 600
            # Get the screen dimension
            screen_width = self.toplevel.winfo_screenwidth()
            screen_height = self.toplevel.winfo_screenheight()
            # Find the center point
            center_x = int(screen_width / 2 - window_width / 2)
            center_y = int(screen_height / 2 - window_height / 2)
            # Set the position of the window to the center of the screen
            self.toplevel.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
            # Window is not resizable
            self.toplevel.resizable(True, True)
            self.puuid = puuid

            self.u = Usecases.Usecases()
            account = self.u.get_specific_account(puuid)
            frame = ctk.CTkFrame(self.toplevel, width=window_width,height=int(window_height*0.8),bg_color="transparent", fg_color="transparent")
            frame.pack(padx=20, pady=20)


            def update_specific_account_and_restart(window, puuid):
                self.u.update_specific_account(puuid)
                window.destroy()
                app_instance = MainWindow()
                app_instance.mainloop()

            update_button = ctk.CTkButton(frame, width=50, fg_color=BUTTON_COLOR , command=lambda puuid=puuid,window=window: update_specific_account_and_restart(window, puuid), text="Update Info", font=(FONT, FONT_SIZE))
            update_button.grid(row=0, column=0, pady=10, padx=PAD_X)

            def remove_specific_account_and_restart(window, puuid):
                self.u.remove_account(puuid)
                window.destroy()
                app_instance = MainWindow()
                app_instance.mainloop()

            remove_button = ctk.CTkButton(frame, width=50, fg_color=BUTTON_COLOR , command=lambda puuid=puuid,window=window: remove_specific_account_and_restart(window, puuid), text="Remove Account", font=(FONT, FONT_SIZE))
            remove_button.grid(row=0, column=1, pady=10, padx=PAD_X)

            def update_password_and_restart(window, puuid):
                new_password = password_entry.get()
                self.u.update_password(puuid, new_password)
                window.destroy()
                app_instance = MainWindow()
                app_instance.mainloop()

            password_entry = ctk.CTkEntry(frame, width=250, placeholder_text="Enter new password")
            password_entry.grid(row=1, column=0, pady=10, padx=PAD_X)
            update_button = ctk.CTkButton(frame, width=50, fg_color=BUTTON_COLOR , command=lambda puuid=puuid,window=window: update_password_and_restart(window, puuid), text="Update Password", font=(FONT, FONT_SIZE))
            update_button.grid(row=1, column=1, pady=10, padx=PAD_X)

            def update_server_and_restart(window, puuid):
                new_server = server_entry.get()
                self.u.update_server(puuid, new_server)
                window.destroy()
                app_instance = MainWindow()
                app_instance.mainloop()

            server_entry = ctk.CTkEntry(frame, width=250, placeholder_text="Enter new server")
            server_entry.grid(row=2, column=0, pady=10, padx=PAD_X)
            update_button = ctk.CTkButton(frame, width=50, fg_color=BUTTON_COLOR , command=lambda puuid=puuid,window=window: update_server_and_restart(window, puuid), text="Update Server", font=(FONT, FONT_SIZE))
            update_button.grid(row=2, column=1, pady=10, padx=PAD_X)

            def update_email_and_restart(window, puuid):
                new_email = email_entry.get()
                self.u.update_email(puuid, new_email)
                window.destroy()
                app_instance = MainWindow()
                app_instance.mainloop()

            email_entry = ctk.CTkEntry(frame, width=250, placeholder_text="Enter new E-Mail")
            email_entry.grid(row=3, column=0, pady=10, padx=PAD_X)
            update_button = ctk.CTkButton(frame, width=50, fg_color=BUTTON_COLOR , command=lambda puuid=puuid,window=window: update_email_and_restart(window, puuid), text="Update E-Mail", font=(FONT, FONT_SIZE))
            update_button.grid(row=3, column=1, pady=10, padx=PAD_X)


            self.toplevel.mainloop()


    class add_account_window():
        def __init__(self, window):
            self.toplevel = ctk.CTkToplevel(window)
            self.toplevel.title("Add Account")
            self.toplevel.transient(window)
            self.toplevel.lift()
            self.toplevel.focus_force() 
            ctk.set_appearance_mode("dark")
            ctk.set_default_color_theme("blue")
            self.toplevel.minsize(800, 600)
            window_width = 800
            window_height = 600
            # Get the screen dimension
            screen_width = self.toplevel.winfo_screenwidth()
            screen_height = self.toplevel.winfo_screenheight()
            # Find the center point
            center_x = int(screen_width / 2 - window_width / 2)
            center_y = int(screen_height / 2 - window_height / 2)
            # Set the position of the window to the center of the screen
            self.toplevel.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
            # Window is not resizable
            self.toplevel.resizable(True, True)

            self.u = Usecases.Usecases()
            frame = ctk.CTkFrame(self.toplevel, width=window_width,height=int(window_height*0.8),bg_color="transparent", fg_color="transparent")
            frame.pack(padx=20, pady=20)

            username_label = ctk.CTkLabel(frame,text="Enter Username: *", font=(FONT, FONT_SIZE))
            username_label.grid(row=0, column=0, pady=10, padx=5)
            username_entry = ctk.CTkEntry(frame, width=250, placeholder_text="Enter username")
            username_entry.grid(row=0, column=1, pady=10, padx=PAD_X)

            tag_label = ctk.CTkLabel(frame,text="Enter Tag: *", font=(FONT, FONT_SIZE))
            tag_label.grid(row=1, column=0, pady=10, padx=5)
            tag_entry = ctk.CTkEntry(frame, width=250, placeholder_text="Enter tag")
            tag_entry.grid(row=1, column=1, pady=10, padx=PAD_X)

            login_label = ctk.CTkLabel(frame,text="Enter Login-Username: *", font=(FONT, FONT_SIZE))
            login_label.grid(row=2, column=0, pady=10, padx=5)
            login_username_entry = ctk.CTkEntry(frame, width=250, placeholder_text="Enter Login-Username")
            login_username_entry.grid(row=2, column=1, pady=10, padx=PAD_X)

            password_label = ctk.CTkLabel(frame,text="Enter password: *", font=(FONT, FONT_SIZE))
            password_label.grid(row=3, column=0, pady=10, padx=5)
            password_entry = ctk.CTkEntry(frame, width=250, placeholder_text="Enter password")
            password_entry.grid(row=3, column=1, pady=10, padx=PAD_X)

            server_label = ctk.CTkLabel(frame,text="Enter Server: ", font=(FONT, FONT_SIZE))
            server_label.grid(row=4, column=0, pady=10, padx=5)
            server_entry = ctk.CTkEntry(frame, width=250, placeholder_text="Enter Server")
            server_entry.grid(row=4, column=1, pady=10, padx=PAD_X)

            email_label = ctk.CTkLabel(frame,text="Enter E-mail: ", font=(FONT, FONT_SIZE))
            email_label.grid(row=5, column=0, pady=10, padx=5)
            email_entry = ctk.CTkEntry(frame, width=250, placeholder_text="Enter E-mail")
            email_entry.grid(row=5, column=1, pady=10, padx=PAD_X)

            def register_new_account_and_restart(window):
                username = username_entry.get()
                tag = tag_entry.get()
                login_username = login_username_entry.get()
                password = password_entry.get()
                server = server_entry.get()
                email = email_entry.get()
                if "" in (username, tag, login_username, password):
                    return
                self.u.register_new_account(username,tag,login_username,password,server,email)

                window.destroy()
                app_instance = MainWindow()
                app_instance.mainloop()

            submit_button = ctk.CTkButton(frame, width=50, fg_color=BUTTON_COLOR , command=lambda window=window: register_new_account_and_restart(window), text="Add Account", font=(FONT, FONT_SIZE))
            submit_button.grid(row=6, column=0, pady=10, padx=PAD_X)

            self.toplevel.mainloop()

    


    class api_window():
        def __init__(self, window):
            self.toplevel = ctk.CTkToplevel(window)
            self.toplevel.title("API Key")
            self.toplevel.transient(window)
            self.toplevel.lift()
            self.toplevel.focus_force() 
            self.database_handler = DatabaseHandler()
            try:
                self.api_key = self.database_handler.get_api_key()
            except IndexError:
                self.api_key = "" 
            ctk.set_appearance_mode("dark")
            ctk.set_default_color_theme("blue")
            self.toplevel.minsize(500, 400)
            window_width = 400
            window_height = 400
            # Get the screen dimension
            screen_width = self.toplevel.winfo_screenwidth()
            screen_height = self.toplevel.winfo_screenheight()
            # Find the center point
            center_x = int(screen_width / 2 - window_width / 2)
            center_y = int(screen_height / 2 - window_height / 2)
            # Set the position of the window to the center of the screen
            self.toplevel.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
            # Window is not resizable
            self.toplevel.resizable(True, True)

            self.u = Usecases.Usecases()
            frame = ctk.CTkFrame(self.toplevel, width=window_width,height=int(window_height*0.8),bg_color="transparent", fg_color="transparent")
            frame.pack(padx=20, pady=20)



            def enter_new_key(window):
                new_key = str(key_entry.get())
                if str(new_key).strip() == "":
                    return

                self.database_handler.update_api_key(new_key)

                window.destroy()
                app_instance = MainWindow()
                app_instance.mainloop()


            label = ctk.CTkLabel(frame,text="Enter new API-KEY: ", font=(FONT, FONT_SIZE))
            label.grid(row=0, column=0, pady=10, padx=5)
            key_entry = ctk.CTkEntry(frame, width=250, placeholder_text="Enter new API-KEY")
            key_entry.grid(row=0, column=1, pady=10, padx=PAD_X)

            submit_button = ctk.CTkButton(frame, width=50, fg_color=BUTTON_COLOR , command=lambda window=window: enter_new_key(window), text="Set new key", font=(FONT, FONT_SIZE))
            submit_button.grid(row=1, column=0, pady=10, padx=PAD_X)

            def open_dev_site():
                webbrowser.open("https://developer.riotgames.com/")

            dev_portal_button = ctk.CTkButton(frame, width=50, fg_color=BUTTON_COLOR , command= open_dev_site , text="Open DevPortal", font=(FONT, FONT_SIZE))
            dev_portal_button.grid(row=1, column=1, pady=10, padx=PAD_X)



    def mainloop(self):
        self.window.mainloop()

if __name__ == "__main__":
    app_instance = MainWindow()
    app_instance.mainloop()