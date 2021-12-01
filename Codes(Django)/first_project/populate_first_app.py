import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

## fake populting script
import random
from first_app.models import Webpage,Topic,AccessRecord
from faker import Faker

fakegen = Faker()
topics= ['Search','Social','Marketpalce','News','Games']

def add_topic():
    t= Topic.objects.get_or_create(top_name=random.choice(topics))[0] #index 0 returns the object created
    t.save()
    return t

def populate(N=5):

    for entry in range(N):

        top = add_topic()

        fake_url=fakegen.url()
        fake_date=fakegen.date()
        fake_name=fakegen.company()

        webpg = Webpage.objects.get_or_create(topic=top,name=fake_name,url=fake_url)[0]

        acc_rec= AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]


if __name__ == '__main__':
    print("population in process")
    populate()
    print("completed populating")
