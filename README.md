# Intel_Project
We First set up a Flask application for a vehicle management system

Following these steps:

Create a project directory>set up a virtual environment>and install Flask.

Structure project with directories for templates (HTML files) and static files (like uploaded images), along with an app.py file for the Flask application.

In app.py, configure routes for different functionalities like uploading images, displaying recognition results, showing parking occupancy, and listing vehicle movements.

Each route renders corresponding HTML templates using Flask's render_template function, and handles file uploads using Flask's request.files module.

Run the application using python app.py,

Running on the server did not work, so we changed it to WSGI Waitress and navigate to <http://0.0.0.0:8000> in browser to interact with the system, which includes tabs for home, image upload, occupancy, recognition results, and vehicle movements.

Currently, there are some issues with the website page running.
