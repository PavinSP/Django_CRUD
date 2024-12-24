# Step 1: Create a virtual environment
## Steps to create a virtual environment:
1) Create a virtual environment
    - python -m venv venv
2) Activate the virtual environment
    - venv/Scripts/activate
# Step 2: Create and host the Django project
## Steps to create and host the Django project:
1) Install Django
    - pip install django
2) Create a Django project
    -  django-admin startproject mysite
3) Navigate to the project directory
    - cd mysite
4) Start the development server
    - python manage.py runserver
7) Open your web browser and navigate to http://localhost:8000
# Step 3: Create an application in the project
## Steps to create an application in the project:
1) Create an application
    - python manage.py startapp app
# Step 4: Create a folder named templates
- Create a HTML file named index.html
- Develop a simple frontend (h1 tag)
# Step 5: Run the index.html instead of the Django template
- In the settings.py of the project folder, you should add app in the INSTALLED_APPS (loads this particular app in the django project)
- In the settings.py of the project folder, include the templates folders in the DIRS key of the dictionary TEMPLATES
- Whenver you are in the home page of the local host, you redirect the path to index.html
    - In the urls.py of the crud folder, add a path that redirects to the urls.py of the application
- In the views.py, define a function to render the request to the index.html 