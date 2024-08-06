"""
cd /Users/sandra/Library/CloudStorage/Dropbox/GooseApp/Algebra_Game/space_gems
deactivate 
source env/bin/activate
pwd
clear;python3 myflask.py
"""
# This file contains the WSGI configuration required to serve up your
# web application at http://<your-username>.pythonanywhere.com/
# It works by setting the variable 'application' to a WSGI handler of some
# description.
#
# The below has been auto-generated for your Flask project
# python3 myflask.py
# python myflask.py
# clear; python3  myflask.py
#http://sanmcc.pythonanywhere.com/


import sys

# add your project directory to the sys.path
project_home = '/Users/sandra/Library/CloudStorage/Dropbox/GooseApp/Algebra_Game/space_gems'
project_home = '/home/JMMM/mysite/'

if project_home not in sys.path:
	sys.path = [project_home] + sys.path

# import flask app but need to call it "application" for WSGI to work
from flask_app import app as application  # noqa

#from flask_app import app as application 
#calls: flask_app,py  NOT application.py

