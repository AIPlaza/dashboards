# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster@sha256:37aa274c2d001f09b14828450d903c55f821c90f225fdfdd80c5180fcca77b3f

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . .

# Expose the port that FastAPI runs on
EXPOSE 8000

# Define environment variable for FastAPI to run in production mode
ENV PYTHONPATH=/app

# Run the application using uvicorn
CMD ["uvicorn", "p2p_api.main:app", "--host", "0.0.0.0", "--port", "8000"]
