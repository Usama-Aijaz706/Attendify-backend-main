#!/bin/bash

# Install CMake and build tools
apt-get update
apt-get install -y cmake build-essential

# Install Python dependencies
pip install -r requirements.txt

# Start the application
uvicorn main:app --host 0.0.0.0 --port $PORT 