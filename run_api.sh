#!/bin/bash
echo "🟢 Starting V2 Backend (FastAPI)..."
cd "$(dirname "$0")"
uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
