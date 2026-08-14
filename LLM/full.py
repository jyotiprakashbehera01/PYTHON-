"""Stateful example: we simulate memory by resending the growing history."""

import os
import requests

API_URL = "https://ollama.com/api/chat"
MODEL = "gpt-oss:20b"
api_key = "2b54b6ccbfb54da59ca41269e9a4b00c.hNHANaRMOkvXxHizHd5ZrLB8"
headers = {"Authorization": f"Bearer {api_key}"}

history = []   # this list IS the memory - the model itself has none

# --- Turn 1: take the first message from the user ---
first_question = input("Enter your first message (e.g. 'My name is Santosh.'): ").strip()
history.append({"role": "user", "content": first_question})
request_1 = {"model": MODEL, "messages": history, "stream": False}
reply_1 = requests.post(API_URL, headers=headers, json=request_1, timeout=120).json()["message"]["content"]
history.append({"role": "assistant", "content": reply_1})
print("Reply 1:", reply_1)

# --- Turn 2: take a follow-up from the user - sends the FULL history, including turn 1 ---
second_question = input("\nEnter your follow-up message (e.g. 'What is my name?'): ").strip()
history.append({"role": "user", "content": second_question})
request_2 = {"model": MODEL, "messages": history, "stream": False}
reply_2 = requests.post(API_URL, headers=headers, json=request_2, timeout=120).json()["message"]["content"]
history.append({"role": "assistant", "content": reply_2})
print("Reply 2:", reply_2)
# The model WILL know the name now (if you mention it in turn 1) -
# because "history" carried turn 1 into turn 2.