# Use the official Python 3.12 image as the base image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Declare environment variables
ENV DISCORD_TOKEN=""
ENV DISCORD_CHANNEL_ID=""
ENV DISCORD_NOTIFICATION_ROLE_ID=""

# Set the default command to run the application
CMD ["python", "main.py"]