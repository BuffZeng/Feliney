from django.db import models

# Create your models here.
class CatProfile(models.Model):
    cid=models.AutoField(primary_key=True)
    breed=models.CharField(max_length=50,null=False)
    price_range=models.CharField(max_length=30)
    friendliness=models.FloatField(default=3.0)
    tidiness=models.FloatField(default=3.0)
    fussiness=models.FloatField(default=3.0)
    description = models.CharField(max_length=800,default="")

    def __str__(self):
        return self.breed