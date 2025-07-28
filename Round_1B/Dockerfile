FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY ./app ./app
COPY ./datasets ./datasets
COPY ./input ./input

# Create output folder if not exists
RUN mkdir -p datasets/output

# Default command to run the main script
CMD ["python", "-m", "app.main"]
