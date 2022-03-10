from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AdminProfile(models.Model):
    aid=models.AutoField(primary_key=True)
    admin = models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    email_id=models.CharField(max_length=50,default=None)
    password=models.CharField(max_length=70,null=False)

    def __str__(self):
        return self.admin.name