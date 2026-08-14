"""Lesson 4: Take live user input and build chat history dynamically."""

import os
import requests

API_URL = "https://ollama.com/api/chat"
MODEL = "gpt-oss:20b"

api_key = "2b54b6ccbfb54da59ca41269e9a4b00c.hNHANaRMOkvXxHizHd5ZrLB8"
if not api_key:
    raise SystemExit("Set OLLAMA_API_KEY first (use your NEW key).")

headers = {"Authorization": f"Bearer {api_key}"}

# Start the conversation with just a system message......
# No hardcoded user/assistant turns - those get built live below.
messages = [
    {
        "role": "system",
        "content": "You are a Python tutor. Answer simply with one example."
    }
]

print(f"Chatting with {MODEL} — type 'exit' to quit.\n")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() in ("exit", "quit"):
        break

    if not user_input:
        continue   # skip empty input, ask again

    # 1. Add the user's new question to history BEFORE sending
    messages.append({"role": "user", "content": user_input})

    request_data = {
        "model": MODEL,
        "messages": messages,   # send the FULL history every time, not just this turn
        "stream": False
    }

    try:
        response = requests.post(API_URL, headers=headers, json=request_data, timeout=120)
        response.raise_for_status()
        result = response.json()

        answer = result["message"]["content"]

        # 2. Add the assistant's reply to history too, so the NEXT
        #    question can refer back to it
        messages.append({"role": "assistant", "content": answer})

        print("Assistant:", answer, "\n")

    except requests.exceptions.HTTPError:
        print("API error:", response.status_code, response.text)
        messages.pop()   # remove the failed user message so retry works cleanly

    except requests.exceptions.ConnectionError:
        print("Could not reach ollama.com. Check your internet connection.")
        messages.pop()

print(f"\nConversation ended. Total messages exchanged: {len(messages) - 1}")