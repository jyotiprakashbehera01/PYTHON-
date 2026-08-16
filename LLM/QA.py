import os # it can interact with operating system , It read envaroment variable .
import re # It mean regular expration , it use later to remove . 
import requests 

API_URL = "https://ollama.com/api/chat" # API_URL is an variable , It store the address of olama API .
MODEL  = "gpt-oss:20b" 
#parameter = Parameters are the learned values inside the AI model.

api_key = "2b54b6ccbfb54da59ca41269e9a4b00c.hNHANaRMOkvXxHizHd5ZrLB8"
#codition
if not api_key:
    raise SystemExit (#stop the program ,It is used because there is no point continuing if the API key doesn't exist.
        "OLLAMA_API_KEY is not set.\n"#Your Ollama API key isn't configured.
        "Windows PowerShell:  $env:OLLAMA_API_KEY=\"your_new_key_here\"\n"# It give comand for windo powercell .
        "Mac/Linux:           export OLLAMA_API_KEY=\"your_new_key_here\""#

    )

SYSTEM_PROMPT = ( #A system prompt tells the AI how it should behave.It is another variable .
    "You are a concise Python tutor. Answer in 3-4 lines maximum. "
    "No long explanations, no repeating the question, no filler. "
    "When comparing two concepts (e.g., list vs tuple), lead with the "
    "single most important difference first (e.g., mutability), then "
    "add only 1-2 supporting details."
)

question = input("You: ").strip()
#input("You: ") : When it asks the user .
#strip() : remove unnessary blank space on satarting and ending .

requests_data = {
        "model" : MODEL ,
         "messages": [ # it has the store messages and send the api is callled list .
             # When the list has content two role 1.system , 2.User .
             
         ]
} 