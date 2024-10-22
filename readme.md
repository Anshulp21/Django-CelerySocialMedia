**Recipe Platform**

# Overview

This project is a social media platform for sharing and rating recipes. Users can upload, share, and rate recipes, with additional features like image resizing, daily email notifications, and CSV exports to S3.


## Features

User authentication (Customers and Sellers)
Rate limiting to prevent abuse
Recipe upload and rating
Image resizing using Celery for optimization
Daily email notifications to keep users engaged
Weekly CSV export to S3 for reporting and analysis

Setup
1. Clone the repository

git clone https://github.com/Anshulp21/Django-Socialmedia.git
cd Django-Socialmedia


2. Install the dependencies
Make sure you have Python and pip installed. Then, run the following command to install required dependencies:

pip install -r requirements.txt

3. Environment Variables
Create a .env file in the project root and add the following configurations:

# AWS Configuration for S3
AWS_ACCESS_KEY_ID=your_access_key_id
AWS_SECRET_ACCESS_KEY=your_secret_access_key
AWS_STORAGE_BUCKET_NAME=your_bucket_name

# Email Configuration
EMAIL_HOST_PASSWORD=your_password_here
EMAIL_HOST_USER=your_email_here

Replace the placeholder values with your actual AWS and email credentials.

4. Run the application
Install Python 3.11: Make sure you have Python 3.11 installed on your system. You can download it from the official Python website.

Create a Virtual Environment: Open your terminal or command prompt and navigate to your project directory. Then, run the following command:

python -m venv my_recipe_app_env

###### Activate Virtual Environment
my_recipe_app_env\Scripts\activate

###### Navigate 
cd recipe_platform

###### Run Redis (make sure Redis is installed and running):
redis-cli

###### Run Django server:
python manage.py runserver

###### Start Celery workers and beat:

celery -A recipe_platform worker --pool=solo --loglevel=info
###### celery -A recipe_platform beat --loglevel=info

5. API Endpoints
Token-based authentication: http://127.0.0.1:8000/api/token/
Recipe management: http://127.0.0.1:8000/api/recipes/
Rate recipes: http://127.0.0.1:8000/api/rate/



###### Additional Commands
###### ### Start Celery worker with solo pool:
celery -A recipe_platform worker -l debug --pool=solo
###### Start Celery worker with concurrency:
celery -A recipe_platform worker --loglevel=info --concurrency=1
###### Debug mode for Celery worker:
celery -A recipe_platform worker --loglevel=debug


**License
This project is licensed under the MIT License.**