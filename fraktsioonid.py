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

        json.dump(andmed, f, indent=4)

def fraktsiooni_liikmed(API_URL):
    response = requests.get(API_URL)
    andmed = response.json()
    for i in range(len(andmed)):
        fraktsiooni_uuid = andmed[i]["uuid"]
        response = requests.get("https://api.riigikogu.ee/api/usergroups/" + fraktsiooni_uuid)
        data = response.json()
        l6pp = []
        print(data)
        with open(f"fraktsioonid\{andmed[i]['name']}.json", "w") as f:
            """            for j in range(len(data["members"])):
                l6pp.append(data["members"][j])"""
            json.dump(data, f, indent=4)

json_faili_loomine(api, "fraktsioonid.json")

fraktsiooni_liikmed(api)
