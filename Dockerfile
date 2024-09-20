# Use an official Python base image
FROM python:3.10.5-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the entire Django project into the container
COPY . /app/

# Expose the port that the Django app will run on
EXPOSE 8080

# Set environment variables for the database (these should be passed at runtime)
ENV DB_NAME=your_db_name
ENV DB_USER=your_db_user
ENV DB_PASSWORD=your_db_password
ENV DB_HOST=your_db_host
ENV DB_PORT=your_db_port

# Run migrations and start the Gunicorn server
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "imgogo.wsgi:application"]
