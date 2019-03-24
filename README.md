OVERVIEW
---- 

Several projects I have worked on have the same basic format:

* Ingest input file(s)
* Perform some calculations and/or modifications
* Display results to user and/or provide a derivative file for download

A web portal is the easiest format for the end-user.

This application is a skeleton for these types of projects. Specifically, to provide most of the 'boilerplate', and for new projects I will only have to modify the templates, and write functions for the specific transformations unique to the project.

Included are:

* Login/logout views
* Upload form view
* Results view
* Optional intermediate step views
** eg. Upload an excel sheet, and then display a preview to the user, and allow him to select a specific column.


Stack:
------
* Python 3.x
* Django 2.x
* Bootstrap 4

Structure:
------
* Standard django project structure.
* Most of the functionality is in app_skeleton/views.py
* Some helper functions are in app_skeleton/helpers.py
* The specific transformations for each particular project will be in app_skeleton/unique_to_this_project.py
* Templates for the various views are in app_skeleton/templates/

A few specifics:
----------
* Uploaded files will go into a folder with a radomly generated name in app_skeleton/UPLOAD/
* Those folders will be cleared out periodcially
* Project contains a sqltile db with a superuser 'admin' with password of 'adminpasswordisverylong'. This should be changed!
* Make sure to add a new ```PROJECT_SECRET``` in project_skelton/settings.py

Files
----
project\_skeleton/  
├── app\_skeleton  
│   ├── admin.py  
│   ├── apps.py  
│   ├── helpers.py  
│   ├── models.py  
│   ├── templates  
│   │   ├── base.html  
│   │   ├── first\_page.html  
│   │   ├── second\_page.html  
│   │   ├── last\_page.html  
│   │   └── registration  
│   │       ├── logged\_out.html  
│   │       └── login.html  
│   ├── tests.py  
│   ├── unique\_to\_this\_project.py  
│   ├── UPLOAD  
│   └── views.py  
├── db.sqlite3  
├── manage.py  
├── project\_skeleton  
│   ├── settings.py  
│   ├── urls.py  
│   └── wsgi.py  
└── README.md




