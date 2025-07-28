# Use a slim Python base image compatible with AMD64
FROM --platform=linux/amd64 python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your Python script into the container
COPY code.py .

# Command to execute your Python script when the container starts
CMD ["python", "code.py"]