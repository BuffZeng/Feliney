import py_compile
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Max
from django.template.defaultfilters import slugify

# Create your models here.
class UserProfile(models.Model):
    uid=models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20)
    name=models.CharField(max_length=50)
    member_since=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    email_id=models.CharField(max_length=50,default=None)
    picture = models.ImageField(null=True,blank=True)
    breeds=models.CharField(max_length=100,null=True)
    about_me=models.CharField(max_length=800)

    def __str__(self):
        return self.user.username

class CatPhotos(models.Model):
    pid=models.AutoField(primary_key=True)
    uid=models.IntegerField()
    picture = models.ImageField(null=True,blank=True)
    uploaddate = models.DateTimeField(auto_now_add=True)
    description=models.CharField(max_length=50,null=True,blank=True)

class CatRatings(models.Model):
    rid=models.AutoField(primary_key=True)
    uid=models.IntegerField()
    cid=models.IntegerField()
    catname=models.CharField(max_length=50)
    fusiness = models.IntegerField()
    friendliness = models.IntegerField()
    tidiness=models.IntegerField()

class Catmessage(models.Model):
    sentdate = models.DateTimeField(auto_now_add=True)
    messageread = models.BooleanField(default=False)
    catmessager = models.ForeignKey(User, on_delete=models.CASCADE,related_name='the_account')
    messagesend = models.ForeignKey(User, on_delete=models.CASCADE,related_name='sending_account')
    messagereceive = models.ForeignKey(User, on_delete=models.CASCADE,related_name='receiving_account')
    messagebody = models.CharField(max_length=600, null=True)
   

class Catimessage(models.Model):
    sentdate = models.DateTimeField(auto_now_add=True)
    messageread = models.BooleanField(default=False)
    catmessager = models.ForeignKey(User, on_delete=models.CASCADE,related_name='usersaccount')
    messagesend = models.ForeignKey(User, on_delete=models.CASCADE,related_name='sendersaccount')
    messagereceive = models.ForeignKey(User, on_delete=models.CASCADE,related_name='receiversaccount')
    messagebody = models.TextField(max_length=600, null=True)
