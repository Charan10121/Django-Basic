from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# models are classes


class Topic(models.Model):  # inherit from models.Model
    top_name = models.CharField(
        max_length=264, unique=True)  # these are constraints

    # str representation of model
    def __str__(self):
        return self.top_name


class Webpage(models.Model):
    # getting key from other table
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)  # typecasting

# class User(models.Model):
#     first_name=models.CharField(max_length=128)
#     last_name=models.CharField(max_length=128)
#     email=models.EmailField(max_length=264,unique=True)



class UserProfileInfo(models.Model):    # model class to add stuff that are not already present
    # create relationship(dont inherit from User)
    user = models.OneToOneField(User,on_delete=models.CASCADE)  # extending the class in a way

    # add any additional attributes
    portfolio_site = models.URLField(blank=True)
    # profile_pics is a sub directory of media
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        # built in attribute of django.contrib.auth.models.User
        return self.user.username
