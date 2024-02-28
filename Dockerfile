# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Install ffmpeg
RUN apt-get update && apt-get install -y ffmpeg

# Install Whisper directly from the GitHub repository
RUN pip install git+https://github.com/openai/whisper.git

# Copy the current directory contents into the container at /app
COPY . /app

# Make index.py executable
RUN chmod +x index.py

# Specify the entry point to make the script executable and allow it to receive arguments
ENTRYPOINT ["python", "/app/index.py"]
