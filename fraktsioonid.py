import requests
import json
import os

api = "https://api.riigikogu.ee/api/usergroups"
lubatud_fraktsioonid = ["Eesti 200 fraktsioon", "Eesti Keskerakonna fraktsioon", "Eesti Reformierakonna fraktsioon", "Sotsiaaldemokraatliku Erakonna fraktsioon", "Eesti Konservatiivse Rahvaerakonna fraktsioon", "Isamaa fraktsioon"]

def json_faili_loomine(API_URL, failinimi):
    response = requests.get(API_URL)
    data = response.json()
    andmed = []
    with open(failinimi, "w") as f:
        for i in range(len(data)):
            if data[i]["name"] in lubatud_fraktsioonid:
                andmed.append(data[i])

        return json.dump(andmed, f, indent=4)

def fraktsiooni_liikmed(rk_api):
    with open("fraktsioonid.json", "r") as f:
        data = json.load(f)
        for i in range(len(data)):
            response = requests.get(rk_api + "/" + str(data[i]["uuid"]))
            data2 = response.json()
            with open(f"fraktsioonid/{data[i]['shortName']}.json", "w") as f2:
                json.dump(data2, f2, indent=4)
                print(f"{data[i]['name']} liikmed on salvestatud faili {data[i]['shortName']}.json")

json_faili_loomine(api, "fraktsioonid.json")

fraktsiooni_liikmed(api)
