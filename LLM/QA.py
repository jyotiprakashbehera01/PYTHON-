"""Lesson 1 (Cloud version): Ask one question using an Ollama cloud model."""

import os
import re
import requests

API_URL = "https://ollama.com/api/chat"
MODEL = "gpt-oss:20b"   # cloud model - swap if you want a different one

api_key = "2b54b6ccbfb54da59ca41269e9a4b00c.hNHANaRMOkvXxHizHd5ZrLB8"
if not api_key:#..
    raise SystemExit(
        "OLLAMA_API_KEY is not set.\n"
        "Windows PowerShell:  $env:OLLAMA_API_KEY=\"your_new_key_here\"\n"
        "Mac/Linux:           export OLLAMA_API_KEY=\"your_new_key_here\""
    )

SYSTEM_PROMPT = (
    "You are a concise Python tutor. Answer in 3-4 lines maximum. "
    "No long explanations, no repeating the question, no filler. "
    "When comparing two concepts (e.g., list vs tuple), lead with the "
    "single most important difference first (e.g., mutability), then "
    "add only 1-2 supporting details."
)

question = input("You: ").strip()

request_data = {
    "model": MODEL,
    "messages": [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": question}
    ],
    "stream": False,
    "options": {
        "temperature": 0.2,
        "num_predict": 300
    }
}

headers = {"Authorization": f"Bearer {api_key}"}

try:
    response = requests.post(API_URL, headers=headers, json=request_data, timeout=180)
    response.raise_for_status()
    result = response.json()

    content = result["message"]["content"].strip()
    content = re.sub(r"<think>.*?</think>", "", content, flags=re.DOTALL).strip()

    print("Assistant:", content if content else "(empty response)")

except requests.exceptions.Timeout:
    print("The request took too long. Try again or use a smaller model.")

except requests.exceptions.ConnectionError:
    print("Could not reach ollama.com. Check your internet connection.")

except requests.exceptions.HTTPError:
    print("API error:", response.status_code, response.text)