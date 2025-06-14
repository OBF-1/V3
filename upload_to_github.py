import base64
import requests

# 🔧 Fill in your real token and details locally
TOKEN = "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"
USERNAME = "OBF-1"
REPO = "V3"
LOCAL_FILE = "backend/main.py"
REMOTE_PATH = "backend/main.py"
COMMIT_MSG = "Add main.py to backend folder"

with open(LOCAL_FILE, "rb") as f:
    content = base64.b64encode(f.read()).decode()

url = f"https://api.github.com/repos/OBF-1/V3/contents/backend/main.py"
headers = {"Authorization": f"token {TOKEN}"}
data = {"message": COMMIT_MSG, "content": content}

response = requests.put(url, headers=headers, json=data)
print(f"Status Code: {response.status_code}")
print(response.json())
