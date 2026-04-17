import APIHandler


class Account():
    def __init__(self, username : str, tag : str, login_username : str, password : str, server="EUW", email=""):
        self.username = username
        self.tag = tag
        self.login_username = login_username
        self.password = password
        self.server = server
        self.email = email
        self.puuid = APIHandler.get_puuid(username, tag)

        info = APIHandler.get_summonerInfo(self.puuid)

        self.division = info["division"]
        self.rank = info["rank"]
        self.lp = info["lp"]
        self.wins = info["wins"]
        self.losses = info["losses"]

    def update_username(self):
        self.username, self.tag = APIHandler.get_summoner_name_from_puuid(self.puuid)
    
    def update_password(self, new_password):
        self.password = new_password

    def update_info(self):
        info = APIHandler.get_summonerInfo(self.puuid)

        self.division = info["division"]
        self.rank = info["rank"]
        self.lp = info["lp"]
        self.wins = info["wins"]
        self.losses = info["losses"]

    def get_login_credentials(self):
        return self.login_username, self.password

if __name__ == "__main__":
    account = Account("ballsohard","EUW", "login_username", "test_password")
    account.username = "test"
    print(account.username)
    account.update_username()
    print(account.username)