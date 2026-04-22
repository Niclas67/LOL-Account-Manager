import requests
import json

#https://developer.riotgames.com/
#API_KEY = "RGAPI-7398a6bc-2cfc-4985-85f9-68708a04e1d5"
#API_KEY = DatabaseHandler.get_api_key()

class AccountNotFoundError(Exception):
    pass


def get_puuid(user_name,riot_id, api_key):
    while True:
        r = requests.get('https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/' + user_name + '/' + riot_id + '?api_key=' + api_key)
        try:
            puuid = json.loads(r.text)['puuid']
            break
        except:
            raise AccountNotFoundError
    return puuid

def get_summonerLevel(puuid, api_key):
    while True:
        r = requests.get('https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/' + puuid + '?api_key=' + api_key)
        try:
            level = json.loads(r.text)['summonerLevel']
            break
        except:
            print("error 2")
            print(r.text)
    return level


def get_summonerInfo(puuid, api_key):
    while True:
        r = requests.get('https://euw1.api.riotgames.com/lol/league/v4/entries/by-puuid/' + puuid + '?api_key=' + api_key)
        break
    if json.loads(r.text) == []:
        info = {
            "division" : "unranked",
            "rank" : "",
            "lp" : "0",
            "wins" : "/",
            "losses" : "/"
        }
    else:
        data = json.loads(r.text)
        info = {}

        for entry in data:
            if entry['queueType'] == 'RANKED_SOLO_5x5':
                info = {
                    "division": entry['tier'],
                    "rank": entry['rank'],
                    "lp": entry['leaguePoints'],
                    "wins": entry['wins'],
                    "losses": entry['losses']
                }
                break

        if not info:
            for entry in data:
                if entry['queueType'] == 'RANKED_FLEX_SR':
                    info = {
                        "division": entry['tier'],
                        "rank": entry['rank'],
                        "lp": entry['leaguePoints'],
                        "wins": entry['wins'],
                        "losses": entry['losses']
                    }
                    break
    return info

def get_info_from_name_riotID(user_name, riot_id, api_key):
    puuid = get_puuid(user_name, riot_id)
    level = get_summonerLevel(puuid)
    info = get_summonerInfo(puuid)
    info['level'] = level
    try:
        info['winrate'] = str(round((info['wins'] / (info['wins'] + info['losses']) * 100),2))+'%'
    except:
        info['winrate'] = "/"
    return info

def get_summoner_name_from_puuid(puuid, api_key):
    r = requests.get("https://europe.api.riotgames.com/riot/account/v1/accounts/by-puuid/" + puuid + '?api_key=' + api_key)
    try:
        data = json.loads(r.text)
        game_name = data['gameName']
        tag_line =  data['tagLine']
    except:
        print("error 2")
        print(r.text)
    return game_name, tag_line



if __name__ == "__main__":
    print(get_summonerInfo("dlksAYa2w6I-W3NscGQatfT89_BHRBH3HnKjpLuzM8itf6fa2tpBsOUKxfhZxEgA-lsmL7WpqbrONQ"))
    #puuid = get_puuid("ballsohard","EUW")
    #print(get_summoner_name_from_puuid(puuid))
    #print(get_summonerID(get_puuid("ballsohard","EUW")))
    #time.sleep(2)
    #print(get_info_from_name_riotID("ballsohard","EUW"))