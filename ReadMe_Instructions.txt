The project has been developed on Python- Django framewoerk. 
I have used Virtual environment to install all the packages so that it doesnot have a dependency
on the system.
The project is currently hosted on localhost:8080.
Base URLs as per instruction in the problem statement as follows- 
Environment Configuration- http://127.0.0.1:8000/rover/environment/configuration/
Update Environment- http://127.0.0.1:8000/rover/environment/
Rover Configuration- http://127.0.0.1:8000/rover/rover/configuration/
Rover move- http://127.0.0.1:8000/rover/rover/move/
Rover status- http://127.0.0.1:8000/rover/rover/status

So the base Url (api as per problem statement) - http://127.0.0.1:8000/rover/
However I have created a navigation panel at the top which will help the user to navigate to any abovementioned page.

Up the server: Instruction for Windows
We have to navigate to ..\mysite\RoverProject directory in cmd and hit the command-
python manage.py runserver
E.g I have kept the mysite folder in the desktop. so I have to navigate to -
C:\Users\"username"\Desktop\mysite\RoverProject

Then fire up the browser and hit any abovementioned URL to get to the app

To go to Django admin, hit URL- http://127.0.0.1:8000/admin/
I have given superuser status to user, so one can check the backend models of django's default view
username- tester, password- rover@20

Github-https://github.com/Skamley/RoverProject
