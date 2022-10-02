from django.db import models
from django.contrib.auth.models import User

class Auth_User(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username=models.CharField(max_length=20)
    email=models.EmailField()
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    is_superuser = models.BooleanField(default=False)
    is_staff= models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login= models.DateTimeField(auto_now=True)
