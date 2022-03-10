from django.db import models
from django.contrib.auth.admin import UserAdmin

# Create your models here.
class AdminProfile(models.Model):
    aid=models.AutoField(primary_key=True)
    admin = models.OneToOneField(UserAdmin, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    email_id=models.CharField(max_length=50,default=None)
    password=models.CharField(max_length=70,null=False)

    def __str__(self):
        return self.admin.name