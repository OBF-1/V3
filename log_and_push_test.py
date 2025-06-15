import os
import shutil
import subprocess
import json
from datetime import datetime
from pathlib import Path
import requests

# Prep folders
logs_root = Path("logs")
previous_path = logs_root / "previous"
if previous_path.exists():
    shutil.rmtree(previous_path, ignore_errors=True)

# Create new session folder
session_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
session_path = logs_root / "sessions" / session_time
session_path.mkdir(parents=True, exist_ok=True)

# Image to test
image_path = "sample.jpg"  # Replace with a valid image path in real use
url = "http://127.0.0.1:8000/analyze-image"

# Send file
print("📤 Sending test image...")
try:
    with open(image_path, "rb") as f:
        response = requests.post(url, files={"file": f})
    response_json = response.json()
    status_code = response.status_code
except Exception as e:
    response_json = str(e)
    status_code = 500

# Save summary
summary = {
    "timestamp": session_time,
    "status_code": status_code,
    "ok": status_code == 200,
    "response": response_json
}
summary_path = session_path / "summary.json"
with open(summary_path, "w") as f:
    json.dump(summary, f, indent=2)

# Git commit
print("⬆️ Committing test logs...")
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", f"Test log {session_time}"])
subprocess.run(["git", "push"])

print(f"✅ Done. Log saved to: {summary_path}")
