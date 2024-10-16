# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables for Flask
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development

# Ensure the instance folder for the SQLite DB exists
RUN mkdir -p /app/instance

# Expose port 5000 to the outside world
EXPOSE 5000

# Add a command to initialize the database
RUN flask db upgrade || true

# Run Flask app with "flask run" to bind to the correct host and port
CMD ["flask", "run"]
