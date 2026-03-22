from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# this is the second approct to coonect our own class to django inuilt class 
# 1st approch is written in user/forms 

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='profile_pictures/profilepic.jpg',upload_to='profile_pictures')
    location= models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
    

# after using imagefield you have to install pillow

# after making class you have to register in . admin.py
