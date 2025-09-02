# Authentication System POC

This project is a Proof of Concept (POC) for a robust authentication system built with Django and Django Rest Framework. It provides a secure way for users to authenticate and manage their sessions.

## Purpose

The primary goal of this project was to implement a secure and flexible authentication system with the following key features:

- **Email-based authentication:** Users register and log in using their email address instead of a username.
- **JWT-based authentication:** The system uses JSON Web Tokens (JWT) for authentication, providing a stateless and secure way to handle user sessions.
- **Logout from all devices:** A critical security feature that allows users to invalidate all their active sessions, effectively logging them out from all devices.
- **User profile API:** An API endpoint that allows authenticated users to view their profile information.

## Features

- **User registration and login:** Users can create an account and log in using their email and password.
- **JWT access and refresh tokens:** The system provides both access and refresh tokens to manage user sessions securely.
- **User profile API:** An endpoint at `/api/accounts/profile/` that returns the user's email and name.
- **Logout from all devices:** An endpoint at `/api/accounts/logout-all/` that invalidates all of a user's active sessions.

## Setup and Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/FazlulAyanKoushik/POC_token_version.git
   ```
2. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the database migrations:**
   ```bash
   python project/manage.py migrate
   ```
4. **Create a superuser:**
   ```bash
   python project/manage.py createsuperuser
   ```
5. **Run the development server:**
   ```bash
   python project/manage.py runserver
   ```

## API Endpoints

- `POST /api/accounts/login/`: User login.
- `POST /api/accounts/logout-all/`: Logout from all devices.
- `GET /api/accounts/profile/`: Get user profile information (requires authentication).
