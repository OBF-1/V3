#!/bin/bash

# Kill any uvicorn server running on port 8000
fuser -k 8000/tcp > /dev/null 2>&1

# Restart FastAPI server
echo "🔄 Starting server..."
uvicorn backend.main:app --port 8000 --reload &

# Wait for server to spin up
sleep 3

# Test upload endpoint using curl
echo "📤 Testing /analyze-image route..."
curl -X POST "http://127.0.0.1:8000/analyze-image" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@test.jpg"

# Done
echo -e "\n✅ Done"
