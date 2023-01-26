# Use an official Ubuntu image as the base
FROM ubuntu:20.04

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y tesseract-ocr

# Install python dependencies
RUN apt-get install -y python3-pip
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Run the command

ENV PORT 8080
ENV HOST 0.0.0.0
EXPOSE 8080:8080

CMD exec uvicorn --port $PORT --host $HOST main:app 