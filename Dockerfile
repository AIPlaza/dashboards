# Use an official Python runtime as a parent image
FROM python:3.11-slim-bullseye

# Set the working directory in the container
WORKDIR /app

# Install Rust and Cargo
RUN apt-get update && apt-get install -y curl
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --default-timeout=120 -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . .

# Expose the port that FastAPI runs on
EXPOSE 8000

# Define environment variable for FastAPI to run in production mode
ENV PYTHONPATH=/app

# Run the application using uvicorn
CMD ["uvicorn", "p2p_api.main:app", "--host", "0.0.0.0", "--port", "8000"]
