from django.db import models
<<<<<<< HEAD
from django.contrib.auth.admin import UserAdmin
=======
from django.contrib.auth.models import User
>>>>>>> 1e07bab4ae2744c81f33bed4078dac48f6dc9fbd

# Create your models here.
<<<<<<< HEAD
=======
class AdminProfile(models.Model):
    aid=models.AutoField(primary_key=True)
<<<<<<< HEAD
    admin = models.OneToOneField(UserAdmin, on_delete=models.CASCADE)
=======
    admin = models.OneToOneField(User, on_delete=models.CASCADE)
>>>>>>> 1e07bab4ae2744c81f33bed4078dac48f6dc9fbd
    name=models.CharField(max_length=50)
    email_id=models.CharField(max_length=50,default=None)
    password=models.CharField(max_length=70,null=False)

    def __str__(self):
        return self.admin.name
>>>>>>> 562e1175e00f40d6eab14586e698807083668470
