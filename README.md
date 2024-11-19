# Reservation App
This is a multi-microservices project built with Python (Django) and Go, designed for seamless reservation management.

## Features
Django Backend: Handles user registration, login, and API requests.

Go API Microservice: Provides internal API functionalities.

Dockerized: Easy setup and deployment with Docker.

## Prerequisites
**Git**: To clone the repository.

- [Download Git](https://git-scm.com/)

**Docker & Docker Compose**: To run the application in containers.

- [Download Docker](https://www.docker.com/products/docker-desktop/)

## Installation Guide
### Step 1: Install Docker
**Follow the instructions for your operating system:**

- **Windows/Mac:**
  - Download and install Docker Desktop from the Docker website.
  - After installation, make sure Docker Desktop is running.
- **Linux:**
  - Use your package manager:
    
    - ``` sudo apt-get update sudo apt-get install -y docker.io docker-compose```
  - Ensure Docker is running:
    
    - ```sudo systemctl start docker sudo systemctl enable docker```
   
### Step 2: Clone the Repository
Use Git to clone the repository:

```git clone https://github.com/yourusername/reservation-app.git```

Navigate to the project directory:

```cd reservation-app```

### Step 3: Build and Run the Docker Containers

1. Make sure Docker is running.
2. Build the Docker containers:
   
   ```docker-compose build```
3. Start the containers:

   ```docker-compose up```

This command will start the backend services (Django and Go).

### Step 4: Access the Application

Once the containers are running:
- **Django Backend:** Accessible at http://localhost:8000.
- **Go Microservice:** Depending on its setup, accessible via the designated port (e.g., http://localhost:8080).

## Stopping the Application
To stop the running containers:

```docker-compose down```

## License
This project is licensed under the MIT License.
