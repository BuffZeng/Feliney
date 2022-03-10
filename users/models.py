import py_compile
from django.db import models
from django.contrib.auth.models import User
from cats.models import CatProfile
from django.template.defaultfilters import slugify

# Create your models here.
class UserProfile(models.Model):
    uid=models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20)
    name=models.CharField(max_length=50)
    member_since=models.CharField(max_length=30)
    email_id=models.CharField(max_length=50,default=None)
    picture = models.ImageField(null=True,blank=True)
    breeds=models.CharField(max_length=100,null=True)
    about_me=models.CharField(max_length=800)

    def __str__(self):
        return self.user.username



class CommentTable(models.Model):
    description = models.CharField(max_length=800,default="")
    uid=models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    cid=models.ForeignKey(CatProfile, on_delete=models.CASCADE)

class CatPhotos(models.Model):
    pid=models.AutoField(primary_key=True)
    uid=models.IntegerField()
    picture = models.ImageField(null=True,blank=True)
    uploaddate = models.DateTimeField(auto_now_add=True)
    description=models.CharField(max_length=50,null=True,blank=True)


