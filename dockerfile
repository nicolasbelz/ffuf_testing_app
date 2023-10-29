# Use a lightweight version of the Python 3.8 image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements.txt from our host to the container
COPY requirements.txt requirements.txt

# Install the required Python packages inside the container
RUN apt update
RUN apt install python3-pip -y
RUN pip3 install Flask
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the Flask application and any other files you have from our host to the container
COPY . .

# Specify the command to run when the container starts
CMD ["python3", "app.py"]
