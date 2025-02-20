# Use an official Python runtime as base image
FROM python:3.9-alpine

# Set the working directory
WORKDIR /app

# Copy application files
COPY . /app

# Install dependencies
RUN pip install flask

# Expose the required port
EXPOSE 8080

# Start the Flask application
CMD ["python", "app.py"]