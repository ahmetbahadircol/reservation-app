# Base image
FROM python:3.12.4-slim

# Set the working directory
WORKDIR /src

# Copy the project files
COPY requirements.txt /src/

# Install dependencies
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . /src

# Expose the port
EXPOSE 8000

# Run the Django app
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
