Reference to use virtual env:
https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

# Using anaconda:
# Create environment with specified python version:
$ conda create --name MyDjangoEnv python=3.6

# List all environments:
$ conda info --envs

# Activate env:
# In MacOS/Linux:
$ source activate MyDjangoEnv
# In Windows:
$ activate MyDjangoEnv

# Install Django:
$ conda install django

# Deactivate env:
$ deactivate


# Using venv:
# Create environment:
$ python -m venv MyDjangoEnv

# Activate env:
# In MacOS/Linux:
$ source MyDjangoEnv/bin/activate

# Update pip
python -m pip install --upgrade pip

# Install Django
pip install django

#to create a new django project
django-admin startproject <nameOfProject>

#to create new application
python manage.py startapp <nameOfApp>

# to runserver
python manange.py runserver

print(__file__)
print(os.path.abspath(__file__))
print(BASE_DIR)
TEMPLATE_DIR = os.path.join(BASE_DIR,"templates")
print(TEMPLATE_DIR)

do not use load staticfiles:  instead use load static

template tags:
use {{ }} for simple text
use {% %} for something like html/css file etc

django models
used to incorporate a database into a django project
django uses SQLite


SQL operates like a giant table
each column has type of field as well
constraints are also there on fields< 'hl'

#for making migrations
python manage.py migrate
python manage.py makemigrations first_app(name of app)
python manange.py migrate


for activating python shell
python manage.py shell


for adding in models through shell
first use the command from first_app(name of app) import Topic(name of class)
t = Topic(top_name="social network")
#this will create a new entry of the class Topic which is already there in models.py with the
#top_name having the value social network
t.save # saves the above created t
print (Topic.objects.all())

#for creating superuser
python manage.py createsuperuser

for populating the database using fake info:(refer: first_project->populate_first_app.py)
use Faker
for running populate_first_app.py in cmd: navigate to parent folder and then use command:
python populate_first_app.py (same as running any python program)

models-templates-views
in views.py import model
use the view to query the model for data that we will need
pass results from the model to the template
edit the template so that it is ready to accept and display the data from the model
map a rule to the view


include in urls:
url(r'try',include('AppTwo.urls')),
if AppTwo.urls contain the following patterns:
urlpatterns = [
    url(r'user/$',views.user,name='users'),
    url(r'help/$',views.help,name='help'),
]
then the above statement (urlurl(r'try',include('AppTwo.urls'))) will find for try in the url
if try is found then it will chop the url from try and match the further url with the urls given in the urlpatterns


Django forms:
create forms.py
similar to model
import to views.py
template tag: {{form}}
get: request data from resource
post: submits data to be processed to a resource
template tag: {{form.as_p}} gives form in top->down manner instead of left->right
always add {% csrf_token %}
cleaned_data is attribute of form to access the data enterd by the user


for converting password to hashes, install libraries:
pip install bcrypt
pip install django[argon2]
Imaging library in python: pillow-> to install: pip install pillow
