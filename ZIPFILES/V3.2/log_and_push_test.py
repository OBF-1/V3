import os
import json
import shutil
import subprocess
import requests
from datetime import datetime

# Set up folder structure
logs_root = "logs"
previous_path = os.path.join(logs_root, "previous")
session_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
session_path = os.path.join(logs_root, "sessions", session_time)
os.makedirs(session_path, exist_ok=True)

# Clean previous logs
if os.path.exists(previous_path):
    shutil.rmtree(previous_path)
os.makedirs(previous_path, exist_ok=True)

# Move old sessions to /previous/
for item in os.listdir(os.path.join(logs_root, "sessions")):
    old = os.path.join(logs_root, "sessions", item)
    if os.path.isdir(old) and session_time not in old:
        shutil.move(old, previous_path)

# Upload test image to API
image_path = "test.jpg"
print("📤 Sending test image...")
with open(image_path, "rb") as img:
    response = requests.post(
        "http://127.0.0.1:8000/analyze-image",
        files={"file": (image_path, img, "image/jpeg")}
    )

# Save JSON output
summary_file = os.path.join(session_path, "summary.json")
summary = {
    "timestamp": session_time,
    "status_code": response.status_code,
    "ok": response.ok,
    "response": response.json() if response.ok else response.text
}
with open(summary_file, "w") as f:
    json.dump(summary, f, indent=2)

# Git commit & push
print("⬆️ Committing test logs...")
subprocess.run(["git", "add", session_path])
subprocess.run(["git", "commit", "-m", f"Test log {session_time}""])
subprocess.run(["git", "push"])

print(f"✅ Done. Log saved to: {summary_file}")
