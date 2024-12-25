# REFER TO THIS LINK FOR THE STEPS TO FOLLOW: https://www.youtube.com/watch?v=Ko5KLX2n334

# Step 1: Create a virtual environment

## Steps to create a virtual environment:

1. Create a virtual environment
   - python -m venv venv
2. Activate the virtual environment
   - venv/Scripts/activate

# Step 2: Create and host the Django project

## Steps to create and host the Django project:

1. Install Django

   ```
   pip install django
   ```

2. Create a Django project

   ```
   django-admin startproject mysite
   ```

3. Navigate to the project directory

   ```
   cd mysite
   ```

4. Start the development server

   ```
   python manage.py runserver
   ```

5. Open your web browser and navigate to http://localhost:8000

# Step 3: Create an application in the project

## Steps to create an application in the project:

1. Create an application
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

# Step 6: Add about.html

- Perform the last two steps from Step 6 for the html file about.html

# Step 7: Add the layout of the getbootstrap.com in the index.html

# Step 8: Modify the index.html

- Add navbar
- Add insert student details component
- Do the same to insert email and age

# Step 9: Dropdown for selecting gender and Submit button

# Step 10: Get the data(name, email, age and gender) with the help of insertData function

# Step 11: Create a database to store the data (in models.py)

- Whenever you make changes in the models.py file, you need to run the migrations.

```
python manage.py makemigrations
```

```
python manage.py migrate
```

# Step 12: Import the Student table from models.py in the views.py file
# Step 13: Register yourself as the admin in the django administrator  
```
python manage.py createsuperuser
```
- The Student table will not be available in the admin panel unless you register yourself as the admin

# Step 14: Displaying the data
- Create a table to display the students data with edit and delete buttons
- Use redirecting to return back to the home page after the data is inserted from /insert

# Step 15: Add functionality to the Edit and Delete buttons

