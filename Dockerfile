# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

ENV OTEL_SERVICE_NAME=jason-python-app
ENV OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf
ENV OTEL_EXPORTER_OTLP_ENDPOINT="https://api.honeycomb.io"
ENV OTEL_EXPORTER_OTLP_HEADERS="x-honeycomb-team=KPWWfxj2uJA0nvNORL0cEB"
    


# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port FastAPI will run on
EXPOSE 8000

# Command to run the FastAPI application
CMD ["opentelemetry-instrument", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]