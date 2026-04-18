import APIHandler


class Account():
    def __init__(self, username : str, tag : str, login_username : str, password : str, server="EUW", email="", puuid=None, division="Unranked", rank="", lp=0, wins=0, losses=0):
        self.username = username
        self.tag = tag
        self.login_username = login_username
        self.password = password
        self.server = server
        self.email = email

        if puuid:
            self.puuid = puuid
        else:
            self.puuid = APIHandler.get_puuid(username, tag)

        self.division = division 
        self.rank = rank
        self.lp = lp
        self.wins = wins
        self.losses = losses

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
        self.update_username()

    def get_login_credentials(self):
        return self.login_username, self.password

    def __str__(self):
        o = f"""
            Username: {self.username}\n
            Tag: {self.tag}\n
            Login Username: {self.login_username}\n
            Password: {self.password}\n
            Server: {self.server}\n
            Email: {self.email}\n
            Puuid: {self.puuid}\n
            Division: {self.division}\n
            Rank: {self.rank}\n
            LP: {self.lp}\n
            Wins: {self.wins}\n
            Losses: {self.losses}
            """
        return o

def register_new_account(username : str, tag : str, login_username : str, password : str, server="EUW", email=""):
    account = Account(username, tag, login_username, password, server, email)
    account.update_info()
    return account


if __name__ == "__main__":
    account = Account("Tibbi","333", "login_username", "test_password")
