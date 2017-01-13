### Requirements
You will need Python installed on your machine (preferably Python3) in order to host the website.
### Virtual Environment Setup
For best practice use a virtual environment when hosting the website. Python3 has a built in capability of creating a virtual environment, from your terminal run the command:
python3 -m venv djangoenv
Here "djangoenv" is the name of the virtual environment.
To activate your virtual environment run the command:
source djangoenv/bin/activate
Any packages you install while the environment is activated will only be installed in your virtual environment and not in your global python install.
If you want to stop using the virtual environment simply run the command:
deactivate
### Download the Repository
You'll need to clone the repository at this step if you haven't already from https://github.com/andrewmil/FeedbackDjango.
### Install Required Packages
While the virtual environment is activated you can install all the required packages using the requirements.txt file in the git repository. Run the following command from the git repository
pip install -r requirements.txt
The packages that are in this file assume the a postgresSQL database is being used. If you wish to use a different type of database you will have to also install the appropriate packages for this.
### Configuring the 'settings.py' File
Most of the settings for the Django site can be edited from the 'settings.py' file found in the 'mysite' folder.
#### Hosting Configuration
If you want the site to be accessible from other machines you'll have to add your IP address to ALLOWED HOSTS array:
ALLOWED_HOSTS=['172.28.XXX.XXX', 'localhost']
'localhost should also be in this array.
#### Database Configuration
Further down in the 'settings.py' file you'll find a piece of JSON data that looks like:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'feedback2',
        'USER': 'andrew',
        'PASSWORD': 'password',
        'HOST': '172.28.XXX.XXX',
        'PORT': '',
    }
}
Reconfigure this file to be able to where your database is hosted. If you wish to use a database other than postgres you will need to change the ENGINE variable. For information on this look in this link https://docs.djangoproject.com/en/1.10/ref/settings/#engine.
### Database Table Format
The table that you are storing in the database will have to be created correctly. The 'database.sql' file contains a command that will create the appropriate table in a postgresSQL database.
You will also have to ensure that the user defined in the 'settings.py' file has the appropriate permissions for the table. In order to grant these permissions on a postgresSQL database use these commands while connected to the database.
GRANT ALL ON feedback TO andrew;
GRANT USAGE, SELECT ON SEQUENCE feedback_id_seq TO andrew;
Where 'andrew' is the name of the user defined in the 'settings.py' file.
### Migrate Database
Once you have confirmed that your database is set up correctly and that the 'settings.py' file details match that of the database return to the root directory of the repository and run the command:
python3 manage.py migrate
This will create the tables that Django requires to be present in your database.
### Run the Site
You should now be able to locally host your the website simply by running the command:
python3 manage.py runserver 0.0.0.0:8001
8001 here is the port chosen to run the website on. You can also just run:
python3 manage.py runserver
which will default to hosting the site on localhost at port 8000.
### Finished!
You should now be able access the webpage at localhost:8001 (or whatever port you chose to host the site on). When you press the submit button on the first page data should be sent to your database.
