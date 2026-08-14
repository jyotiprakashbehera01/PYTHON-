"""Stateless example: each request is independent - no memory between calls."""

import os
import requests

API_URL = "https://ollama.com/api/chat"
MODEL = "gpt-oss:20b"
api_key = "2b54b6ccbfb54da59ca41269e9a4b00c.hNHANaRMOkvXxHizHd5ZrLB8"
headers = {"Authorization": f"Bearer {api_key}"}

# --- Call 1: take the first message from the user ---
first_question = input("Enter your first message (e.g. 'My name is Santosh.'): ").strip()

request_1 = {
    "model": MODEL,
    "messages": [{"role": "user", "content": first_question}],
    "stream": False
}
response_1 = requests.post(API_URL, headers=headers, json=request_1, timeout=120)
print("Reply 1:", response_1.json()["message"]["content"])

# --- Call 2: a brand new, separate request - take a second message from the user ---
second_question = input("\nEnter your second message (e.g. 'What is my name?'): ").strip()

request_2 = {
    "model": MODEL,
    "messages": [{"role": "user", "content": second_question}],
    "stream": False
}
response_2 = requests.post(API_URL, headers=headers, json=request_2, timeout=120)
print("Reply 2:", response_2.json()["message"]["content"])
# The model will NOT know anything from Call 1 - request_2 has no idea request_1 ever happened.