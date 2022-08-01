# django-database-connection

#-----------heres the main urls code since i got the same name it cant be posted--------------------------------

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include("enterdata.urls")),
    path('admin/', admin.site.urls),
]
-----------------------------------------------------------------------------------------------------------------
# Create a folder active virtual environment create project folder (django admin startproject (folder name)
step1:Creat a html template

2: create data base in xampp and host it

3:create an application in django using python manage.py startapp ((hello)name) in cmd

4:in the application hello tap on models.py and create a class and define the inputs you have given in your html template

5:tap on views.py 

6:urls.py(create a file)

7:settings.py

8:urls.py

cmd-- python manage.py make migrations

cmd-- python manage.py migrate

cmd-- python manage.py runserver

there you go your all set with your data base connection and make sure to keep your xampp on while migrations and migrate.
