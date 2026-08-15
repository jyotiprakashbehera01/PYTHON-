import requests
#import is the request library .
#request communicate with the website/API's .
api_key = "2b54b6ccbfb54da59ca41269e9a4b00c.hNHANaRMOkvXxHizHd5ZrLB8"
#API_KEY is like a code/token that taill the server .
#When API_KEY are the store innside the variable .
resp = requests.get(
    #GET is request to the srever .
    #GET is genaraly use retrive/read information .
    #requests.get() do : It send the http get request in the specific  url and return the server responce .
     "https://ollama.com/v1/models",
     # this the API endpoint.
     # It give them specific model v1/models. 
     headers={"Authorization":f"Bearer{api_key}"}
     # header conten t extra innformation abhove the http request .
     # hear we send authorixzatio token .
     # Bearer tail the server it has authorization token .
)
for model in resp.json()["data"]:
    #The API response is usually JSON.JSON looks similar to Python dictionaries/lists.
    print(model["id"])

 # output :
#     deepseek-v4-pro:preview
# minimax-m3
# glm-5.2
# gemma4:31b
# kimi-k2.7-code
# gpt-oss:20b
# nemotron-3-ultra
# kimi-k2.6
# gpt-oss:120b
# nemotron-3-nano:30b
# qwen3.5:397b
# deepseek-v4-flash:0731
# minimax-m2.7
# nemotron-3-super
# kimi-k3
# deepseek-v4-flash:preview
# mistral-large-3:675b
# glm-5.1