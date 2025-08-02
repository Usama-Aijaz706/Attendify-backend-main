#!/bin/bash

# Install system dependencies for dlib
apt-get update
apt-get install -y \
    cmake \
    build-essential \
    libopenblas-dev \
    liblapack-dev \
    libx11-dev \
    libsm6 \
    libxext6 \
    libxrender-dev

# Install Python dependencies
pip install -r requirements.txt

# Start the FastAPI application
uvicorn main:app --host 0.0.0.0 --port 8000 