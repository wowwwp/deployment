FROM python:3.9-slim

WORKDIR /app

# Create a directory for the audio files to be mounted (testing purposes)
RUN mkdir /app/cv-valid-dev

# Copy the current directory contents into the container at /app
COPY asr_api.py /app
COPY requirements.txt /app

# Install required Python dependencies
RUN pip install -r requirements.txt

# Expose port if the API is running on a specific port
EXPOSE 8001

# Command to run the API 
CMD ["flask", "--app", "asr_api.py", "run", "--host=0.0.0.0", "--port=8001"]
