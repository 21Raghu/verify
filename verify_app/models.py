from django.db import models
# Create your models here.
class User_Emp(models.Model):
    id = models.IntegerField(primary_key=True)
    email=models.EmailField()
    first_name = models.CharField(max_length=40)
    last_name= models.CharField(max_length=40)
    #avatar=models.ImageField()