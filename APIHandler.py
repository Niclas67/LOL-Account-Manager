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
    print(api_key)
    print(puuid)
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
    puuid = get_puuid(user_name, riot_id, api_key)
    level = get_summonerLevel(puuid, api_key)
    info = get_summonerInfo(puuid, api_key)
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
    DEVELOPEMENT_API_KEY = "RGAPI-12a9a45e-82b8-45f1-a94f-2b707ad42646"
    APP_API_KEY = "RGAPI-4b23fda7-0a52-4db3-87c7-6a9a098920de"
    
    #puuid = get_puuid("Lexie Liu","vbuck",APP_API_KEY)
    #summoner_level = get_summonerLevel(puuid, APP_API_KEY)
    #summoner_info = get_summonerInfo(puuid, APP_API_KEY)
    #summoner_name = get_summoner_name_from_puuid(puuid, APP_API_KEY)
    #summoner_info = get_info_from_name_riotID("Lexie Liu", "vbuck", APP_API_KEY)
    #result = get_summonerInfo("dlksAYa2w6I-W3NscGQatfT89_BHRBH3HnKjpLuzM8itf6fa2tpBsOUKxfhZxEgA-lsmL7WpqbrONQ", "RGAPI-7f716779-5917-4c25-854c-6cf19866dbf7")
    #print(result)
    puuid = get_puuid("Lexie Liu","vbuck",APP_API_KEY)
    print(puuid)
    print(puuid == "3V_31lUTMDxNzPZXPShMtVN3eqfI2zKHcyvXrVuRornpXUxpJQswijDYzmZ8gayNQetCkF0Ds9w-1g")