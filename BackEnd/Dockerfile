# backend/Dockerfile
FROM python:3.12-slim

WORKDIR /PitStopNews/Backend

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . /PitStopNews/Backend

# Expose the Flask port
EXPOSE 5000

# Command to run the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]
