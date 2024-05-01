import datetime
import requests
import json

algus_kuup2ev = "2023-04-01"
t2nane_kuup2ev = datetime.datetime.today().strftime("%Y-%m-%d")

def kohaloleku_kontrollid(json):
    response = requests.get(json)
    data = response.json()
    print(len(data))
    for i in range(len(data)):
        if data[i]["votings"]:
            if data[i]["votings"][0]["type"]["value"] == "Kohaloleku kontroll":
                print(f"{str(data[i]["votings"][0]["uuid"])}")
kohaloleku_kontrollid(f"https://api.riigikogu.ee/api/votings?endDate={t2nane_kuup2ev}&lang=ET&startDate={algus_kuup2ev}")