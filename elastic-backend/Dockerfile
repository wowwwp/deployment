# Step 1: Start with the official Python image
FROM python:3.9-slim

WORKDIR /app

RUN pip install --no-cache-dir pandas elasticsearch==2.4.1

COPY cv-index.py /app/cv-index.py

COPY cv-valid-dev.csv /app/cv-valid-dev.csv

# Step 5: Run the Python script
CMD ["python", "cv-index.py"]
