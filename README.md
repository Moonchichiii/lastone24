# last_backend5

# Recipe Repository Backend

[Click here for the Frontend Repository](#)

[Click here for Live site](#)

## Table of Contents

1.  [Project Goals](#project-goals)
2.  [User Stories](#user-stories)
3.  [Database Management](#database-management)
4.  [Backend Structure and Setup](#backend-structure-and-setup)
5.  [API Endpoints](#api-endpoints)
6.  [Technologies Used](#technologies-used)
7.  [Dependencies](#dependencies)
8.  [Testing](#testing)
9.  [Deployment](#deployment)
10.  [Credits & Tutorials](#credits-&-tutorials)

----------

## Project Goals  

The goal of this project is to develop a simple snappy, mobile-first social food posting website/application. 
The platform allows users to view and search for food posts without logging in.
Once logged in, users are directed to a dashboard with functionalities such as feed, liked posts, profile page, and post new recipe post.

----------

## User Stories 

1.  **As a Visitor**, I want to view and search for food posts without logging in, so I can explore content freely.  
2.  **As a User**, I need to register and log in, so I can access personalized features like my dashboard. 
3.  **As a User**, I want to navigate through different sections such as feed, liked posts, and my posts, for an organized view of content.
4.  **As a User**, I wish to post new recipes, so I can share my culinary creations with the community.
5.  **As a User**, I want to follow other profiles and like posts, to engage with the community.

[Back to top](#table-of-contents)
----------

## Database Management


<img src="dbschema" alt="database schema" width="320">


[Back to top](#table-of-contents)
----------

## Backend Structure and Setup

## Overview

-   **drf**: This is the main project folder. It contains the global settings and configurations that apply to the entire project.    
-   **utils**: This app provides shared services across the project. It includes important functions like handling images for both profiles and posts, managing permissions within the app, and validating image uploads.
-   **users**: App that handles user registration, along with login and logout processes. It ensures users can securely access their accounts.    
-   **profiles**: Manages everything related to user profiles. This includes updating public profile information and displaying it to other users.    
-   **posts**: The core app where recipe posts are managed. Here, users can create, view, update, or delete recipe posts.    
-   **comments**: Responsible for managing comments. This app allows users to add comments to posts and also links these comments with the respective posts.    
-   **likes**: This app takes care of the 'likes' feature. Users can 'like' posts, and this app manages these interactions and links them with the relevant posts.    
-   **followers**: Handles the functionality that lets profiles follow other profiles. About creating connections between different profiles.    


### Setting Up the Project

To set up the project, follow these steps:

1.  **Start a Django Project**:

`django-admin startproject drf .`

This creates the main project folder and the necessary files for the Django project.

2.  **Create Django Apps**: Navigate to the project directory and create the Django apps.

`django-admin startapp comments`

`django-admin startapp followers`
`django-admin startapp likes`
`django-admin startapp posts`
`django-admin startapp profiles`
`django-admin startapp users`
`django-admin startapp utils `

Each command creates a new app with its respective folder and basic files.
Then add urls.py and serializers.py in each app folder and link it back to the project urls.py. 

3.  **Configure Installed Apps**: Add the created apps to the `INSTALLED_APPS` list in `settings.py`
INSTALLED_APPS = [
`'cloudinary_storage',`
`'django.contrib.staticfiles',`
`'cloudinary',`
`'corsheaders',`
`'rest_framework',`
`'comments',`
`'followers',`
`'likes',`
`'posts',`
`'profiles',`
`'users',`
`'utils',`
]

4.  **Database Migrations**: After creating your models, run migrations to create the necessary database tables.

`python manage.py makemigrations`

`python manage.py migrate`

5.  **Run the Development Server**: To start the Django development server, run:

`python manage.py runserver`

This will start a local server

[Back to top](#table-of-contents)

----------

[Back to top](#table-of-contents)
----------

## API Endpoints

-  **GET /posts/**: Retrieve a list of posts. -
-  **POST /posts/**: Create a new post. Title and content in the request. -
-  **GET /posts/{id}/**: Retrieve details of a specific post. -
-  **PUT /posts/{id}/**: Update a specific post. Title and content in the request. -
-  **DELETE /posts/{id}/**: Delete a specific post.

[Back to top](#table-of-contents)
----------

## Technologies Used
  
The backend repository is built and managed using these technologies.
-  **Python**: The core programming language of the project.
-  **Vs Code**: Visual Studio Code editor.
-  **Django**: A Python web framework employed for its ability to facilitate rapid development, serving as the backbone of the backend architecture.
-  **Heroku**: Utilized as the cloud platform for deploying and hosting the application.

-  **PostgreSQL on Heroku**: Reliability, serves as the primary database for the application, hosted on Heroku.
-  **Cloudinary**: Integrated for management and hosting of images, ensuring optimized media storage and delivery.
-  **GitHub**: Used for version control and source code management, tracking of changes throughout the development.

[Back to top](#table-of-contents)
----------

## Dependencies

Various libraries and frameworks used in this project:

asgiref (3.7.2): Enables async features in Django, such as async views and middleware.
cloudinary (1.37.0): Manages cloud-based image and media assets efficiently.
coverage (7.4.0): Measures code coverage to ensure thorough testing.
dj-database-url (2.1.0): Simplifies database configuration for flexible deployment.
django-cors-headers (4.3.1): Controls CORS settings for secure cross-domain access.
Django (5.0.1): The primary framework for web development.
django-filter (23.5): Filters querysets based on request parameters.
djangorestframework (3.14.0): Toolkit for building Web APIs.
djangorestframework-simplejwt (5.3.1): Adds JWT authentication for APIs.
drf-spectacular (0.27.0): Generates OpenAPI schema for API documentation.
dj3-cloudinary-storage (0.0.6): Integrates Cloudinary for media management.
gunicorn (21.2.0): Serves the Django app in production environments.
pillow (10.1.0): Supports image processing tasks.
psycopg2-binary (2.9.9): Connects to PostgreSQL databases.
python-decouple (3.8): Manages configuration variables outside the codebase.
pytz (2023.3): Provides timezone support.
requests (2.31.0): Facilitates HTTP requests for external APIs.
sqlparse (0.4.2): Assists in formatting and parsing SQL queries.
urllib3 (1.26.9): Powers HTTP communication for the requests library.

[Back to top](#table-of-contents)
----------

## Testing

I've used Postman and unitest for testing the project to make sure everything works as intended. 

### Postman for API Testing
Postman was used for checking the API endpoints. 

User Registration:
Method: POST

<img src="register.png" alt="registration" width="320">



User Login:
Method: POST

<img src="login" alt="login" width="320">



User Logout:
Clearing the token. 

Method: POST

<img src="logout" alt="logout" width="320">

### Pytest for Unit Testing

Pytest for unit testing, ensuring individual code component functions as planned. 

<img src="coverage" alt="coverage" width="320">



[Back to top](#table-of-contents)
----------

## ## Deployment

### Key Settings and Preparations

Before deploying, check following:

-   **Environment Variables**: Sensitive information and configuration settings are managed using `decouple`. Ensures sensetive variables are not exposed in the codebase.
-   **Production Settings**: Switch off any development settings, like `DEBUG`, for security and performance optimization.

### Deployment Process

The deployment involves the following steps:

1.  **Local Development**: After making changes locally, push the updated code to GitHub.
2.  **GitHub to Heroku**: Connect the GitHub repository to Heroku. This can be done via the Heroku dashboard.
3.  **Deploy on Heroku**: Used Herokus dashboard to deploy the application. Allows for viewing of logs and managing deployments.
4.  **Monitoring**: Post-deployment, Heroku logs are useful for monitoring and troubleshooting any issues not encountered during development.

[Back to top](#table-of-contents)
----------

## Credits & Tutorials

### README Management

- [https://stackedit.io](https://stackedit.io/)
- [https://django-rest-framework-simplejwt.readthedocs.io/_/downloads/en/latest/pdf/] (DRF Simple jwt docs)
- [https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies#restrict_access_to_cookies] (Cookies to cookies)

[Back to top](#table-of-contents)






