from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    picture=models.ImageField(default='defaultprofile.svg', upload_to='users')
    country=models.CharField(max_length=100, null=True, blank=True)
    provinces=models.CharField(max_length=100, null=True, blank=True)
    
    USER_TYPE_CHOICES = (
        ('client', 'Client'),
        ('photographer','Photographer'),
    )
    usertype = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='client')

class userPhotographer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='photographer')
    specialty = models.CharField(max_length=100, null=True, blank=True)
    phone_number= models.CharField(max_length=15, null=True, blank=True)

