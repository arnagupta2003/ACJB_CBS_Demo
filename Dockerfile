# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any necessary dependencies specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port 8000 for Django
EXPOSE 8000

# Set environment variables for Django settings
ENV DJANGO_SETTINGS_MODULE=hello_world.settings
ENV PYTHONUNBUFFERED=1

# Run migrations and start Django development server
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
