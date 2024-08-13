# Decentralized Chat Application

This is a basic peer-to-peer chat application built using Django and Django Channels. It allows for real-time messaging between users over WebSocket connections. This project is designed to be a simple implementation of a decentralized chat system.

## Prerequisites

Before you can run this project, you'll need to have the following installed on your local machine:

- Python 3.8+
- Django 4.x
- Django Channels

## Installation

Follow these steps to set up and run the application locally:

### 1. Clone the Repository

```bash
https://github.com/shivang257/Decentralized-Chat-Application.git
cd Decentralized-Chat-Application
cd chatproject
```

### 2. Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Apply Migrations
```bash
python manage.py migrate
```

### 4. Run the Development Server
```bash
python manage.py runserver
```

If requirements.txt doesn't exist, you can manually install the necessary packages:
```bash
pip install django channels
```
