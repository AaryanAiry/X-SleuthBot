# Use official Python image
FROM python:3.13.5

# Set working directory inside container
WORKDIR /app

# Copy only what we need (excluding .env and __pycache__)
COPY requirements.txt .
COPY *.py .
COPY *.csv .
COPY *.png .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Default command (no entrypoint since scripts are independent)
CMD [ "bash" ]
