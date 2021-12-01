import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','proTwo.settings')

import django
django.setup()

# script starts here
import random
from AppTwo.models import User_details
from faker import Faker

fakegen=Faker()

def populate(N=5):

    for entry in range(N):
        fake_name=fakegen.name().split();
        fake_fname=fake_name[0]
        fake_lname=fake_name[1]
        fake_email=fakegen.email

        #adduser
        user=User_details.objects.get_or_create(f_name=fake_fname,
                                                l_name=fake_lname,
                                                email=fake_email,
                                                )

if __name__ == '__main__':
    print("populating")
    populate(10)
    print("finished populating")
