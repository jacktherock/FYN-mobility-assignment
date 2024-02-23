# Pricing Module

The Pricing Module is a web application designed for storing and managing product/service prices. It also includes functionality to calculate the final invoice amount based on various parameters such as distance traveled, ride time, and waiting time.

## Features

- Store and manage pricing configurations.
- Calculate pricing based on predefined formulas.
- View logs of configuration changes.

## Technologies Used

- **Backend**: Django
- **Frontend**: React.js
- **Database**: Django's default database (SQLite)
- **API Framework**: Django REST Framework

## Setup

### Backend (Django)

1. Clone the repository:

   ```bash
   git clone https://github.com/jacktherock/FYN-mobility-assignment
   cd FYN-mobility-assignment
   cd backend
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv env
   .\env\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```bash
   python manage.py migrate
   ```

5. Create a superuser (for accessing the Django admin):

   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:

   ```bash
   python manage.py runserver
   ```

7. Access the admin interface at `http://localhost:8000/admin` and log in with the superuser credentials.

### Frontend (React.js)

1. Navigate to the `frontend` directory:

   ```bash
   cd frontend
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Start the development server:

   ```bash
   npm start
   ```

4. Access the frontend interface at `http://localhost:5173`.

## Usage

- Use the Django admin interface to add, modify, or delete and manage pricing configurations.
- Access the React frontend to view pricing configurations.

## API Endpoints

- **/api/pricing_config/**
