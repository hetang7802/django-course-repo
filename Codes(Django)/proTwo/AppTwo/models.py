from django.db import models

# Create your models here.

class User_details(models.Model):
    f_name=models.CharField(max_length=264)
    l_name=models.CharField(max_length=264)
    email=models.EmailField(max_length=264,unique=True)
    def __str__(self):
        return self.f_name
