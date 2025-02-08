from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Account(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_images/', default='profile_images/default.png')
    profile_comment = models.TextField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.user_id.username

