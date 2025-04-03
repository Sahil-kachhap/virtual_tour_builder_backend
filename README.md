# Virtual Tour Builder - Backend Implementation

This repository contains the Django backend implementation for the Virtual Tour Builder application. This README provides guidance on setting up the development environment and getting started with the project.

## Project Overview

The Virtual Tour Builder backend is built with Django and Django REST Framework. It provides a secure API to manage virtual tours, user management, locations, and reviews. The system integrates with Google Maps API for geolocation data and Google Street View API for 360° imagery.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- MySQL database
- Google Maps API key (for location services)
- Google Street View API key (for panoramic imagery)

### Setting Up the Development Environment

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd virtual-tour-builder
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv

   # On Windows
   venv\Scripts\activate

   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root directory using the provided template:

   ```bash
   cp .env.example .env
   ```

   Update the environment variables with your configuration.

5. Create a PostgreSQL database and update the .env file with the credentials.

6. Apply migrations:

   ```bash
   python manage.py migrate
   ```

7. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

8. Run the development server:
   ```bash
   python manage.py runserver
   ```

### Project Structure

The backend is organized into the following Django apps:

- **users**: Manages authentication and user roles
- **tours**: Handles virtual tour creation and management
- **locations**: Stores and retrieves location data
- **reviews**: Implements user feedback and ratings
- **permissions**: Manages role-based access control

### API Documentation

API documentation is available at:

- Swagger UI: `/swagger/`
- ReDoc: `/redoc/`

### Authentication

The API uses JWT authentication. To authenticate:

1. Obtain an access token using the `/api/token/` endpoint
2. Include the token in the Authorization header: `Authorization: Bearer <token>`

### User Roles

The system supports three user roles:

1. **Admin**: Full access to all features
2. **Editor**: Can create and manage tours and content
3. **Viewer**: Can view tours and submit reviews

## Development Workflow

Please follow these guidelines during development:

1. Create feature branches from the `develop` branch
2. Write tests for new functionality
3. Follow PEP 8 style guidelines
4. Document API endpoints and functions
5. Submit pull requests for code review

## Deployment

For production deployment, follow the instructions in the `deployment.sh` script. This will set up the application with Gunicorn and Nginx.

## External API Integration

The system integrates with the following external APIs:

- **Google Maps API**: For geolocation and mapping
- **Google Street View API**: For 360° panoramic imagery

Make sure you have valid API keys configured in the `.env` file.

## Support

If you have any questions or need help, please contact the project supervisor.

Good luck with your implementation!
