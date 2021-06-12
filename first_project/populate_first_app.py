import os
from typing import Mapping

import faker
#configure the settings for the project
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

#fake population script
import random
from first_app.models import Webpage,AccessRecord,Topic
from faker import Faker

fakegen = Faker()    #instance of the object
topics = ['Search','Social','Marketplace','News','Games'] #list of topics

def add_topic():
    #similar to shell command line
    #get topic, if exists, else create it
    #get_or_create is a tuple and [0] refers to model instance
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range (N):
        top=add_topic()

        #create fake data
        fake_url=fakegen.url()
        fake_date=fakegen.date()
        fake_name=fakegen.company()

        #create new webpage entry
        webpg=Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        #create fake access record for that web page
        acc_rec=AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__=='__main__':
    print('populating script')
    populate(20)
    print('done populating')