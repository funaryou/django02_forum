from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Account(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_images/', default='profile_images/default.png')

    def __str__(self):
        return self.user.username
