import requests

api_key = "2b54b6ccbfb54da59ca41269e9a4b00c.hNHANaRMOkvXxHizHd5ZrLB8"

resp = requests.get(
    "https://ollama.com/v1/models",

    headers={"Authorization":f"Bearer{api_key}"}
)

for model in resp.json()["data"]:
    print(model["id"])
#....
