# Use the Python 3.9 image based on Alpine Linux
FROM python:3.9-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apk update && \
    apk add --no-cache postgresql-dev && \
    apk add --no-cache gcc musl-dev

# Create and set the working directory
WORKDIR /code

# Copy the requirements file into the container
COPY requirements.txt /code/

# Upgrade pip
RUN pip install --upgrade pip

# Install Python packages from requirements.txt
RUN pip install -r requirements.txt

# Expose port 8888 (if your Django app uses this port)
EXPOSE 8888

# Define the command to run your Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8888"]

