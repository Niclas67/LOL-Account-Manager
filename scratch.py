import requests

api_key = "RGAPI-b50a50d2-c050-402d-94b8-6147aad73f90"

r = requests.get(
    "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/SR5QNdUQ1P8804k18gUSOyBc6qSaxHjljnLdur8Qia3QXIAOzDn3fVLPCRey09qa4nhs18hFyy74bg",
    headers={"X-Riot-Token": api_key}
)

print(r.status_code)
print(r.text)


