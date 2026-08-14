"""Lesson 2: Understand the request and extract response details (Cloud version)."""

import os
import json
import requests

API_URL = "https://ollama.com/api/chat"
MODEL = "gpt-oss:20b"

api_key = "2b54b6ccbfb54da59ca41269e9a4b00c.hNHANaRMOkvXxHizHd5ZrLB8"

if not api_key:#...
    raise SystemExit("Set OLLAMA_API_KEY first (use your NEW key, not the old exposed one).")

request_data = {
    "model": MODEL,
    "messages": [
        {"role": "user", "content": "Explain a Python list in two lines."}
    ],
    "stream": False
}

headers = {"Authorization": f"Bearer {api_key}"}

response = requests.post(API_URL, headers=headers, json=request_data, timeout=120)
result = response.json()

# ---- 1. See the RAW response first - this is what actually comes back ----
print("=== RAW JSON RESPONSE ===")
print(json.dumps(result, indent=2))

# ---- 2. Now pull out each field individually, with what it means ----
print("\n=== FIELD-BY-FIELD BREAKDOWN ===")

print("Status code:", response.status_code)
# 200 = success. 401 = bad/missing API key. 404 = model name doesn't exist.

print("Model:", result["model"])
# Confirms which model actually answered - useful when testing multiple models.

print("Created at:", result["created_at"])
# UTC timestamp of when the response was generated.

print("Role:", result["message"]["role"])
# Always "assistant" for the model's reply (vs "user" or "system" in your request).

print("Answer:", result["message"]["content"])
# The actual text you want - this is the only field most apps really need.

print("Done:", result["done"])
# True = the full response was generated. False would mean it's mid-stream
# (only relevant if stream=True, which we're not using here).

print("Done reason:", result.get("done_reason"))
# "stop" = model finished naturally. "length" = it got cut off by num_predict.

print("Input tokens (prompt_eval_count):", result.get("prompt_eval_count", 0))
# How many tokens your PROMPT used - this is what you're billed/rate-limited on (input side).

print("Output tokens (eval_count):", result.get("eval_count", 0))
# How many tokens the MODEL'S ANSWER used - billed/rate-limited on the output side.(out put token)

# ---- 3. Timing fields come in NANOSECONDS - convert to seconds to read them ----
total_duration_s = result.get("total_duration", 0) / 1_000_000_000
eval_duration_s = result.get("eval_duration", 0) / 1_000_000_000

print(f"Total time: {total_duration_s:.2f}s")
# Full round-trip time for the whole request.

print(f"Generation time: {eval_duration_s:.2f}s")
# Time spent just generating the output tokens (excludes network/queue time).

if result.get("eval_count") and eval_duration_s > 0:
    tokens_per_sec = result["eval_count"] / eval_duration_s
    print(f"Speed: {tokens_per_sec:.1f} tokens/sec")
    # Handy metric for comparing model speed across different cloud models.