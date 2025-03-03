# Use official Python runtime as a base image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Install system dependencies required for fast-alpr (e.g., OpenCV, Tesseract)
RUN apt-get update && apt-get install -y \
    libopencv-dev \
    tesseract-ocr \
    libtesseract-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file (optional, if you have one) or install directly
# Here we install fast-alpr and fastapi directly
RUN pip install --no-cache-dir fastapi[standard] fast-alpr 

# Copy your application code into the container
COPY . /app

# Expose port 8000 for FastAPI
EXPOSE 8000

# Command to run the FastAPI app with Uvicorn
CMD ["fastapi", "dev", "index.py", "--host", "0.0.0.0", "--port", "8000"]
