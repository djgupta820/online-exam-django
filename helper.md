# to create virtual environment
py -m venv env 

# to activate virtaul environment
venv\Scripts\activate

# to install django (in venv)
pip install django

# to check django installed successfully or not (django version)
django-admin --version
 
# to get all django-admin commands
django-admin --help

# to create or start a project
django-admin startproject <project_name> (onlineexam)

#! now change the working directory to project directory
cd <directory_name> (onlineexam)

# to run the django server
py manage.py runserver

# in settings file under the TEMPLATES list put "templates" in "dirs" list to register the templates folder

