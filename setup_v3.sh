#!/bin/bash
echo "📦 Unzipping V3.4.zip..."
unzip -o V3.4.zip -d V3.4

echo "📁 Switching to V3.4..."
cd V3.4 || exit

echo "📦 Installing Python dependencies..."
pip install -r requirements.txt || {
  pip install fastapi uvicorn diffusers torch torchvision accelerate safetensors transformers pillow
}

echo "✅ Setup complete. Run the backend with:"
echo "uvicorn backend.main:app --host 0.0.0.0 --port 8000"
