from datetime import timezone
from django.db import models

from rest.models import User

# Create your models here.
class Record(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)
    #updatedAt = models.DateTimeField(default=timezone.now, editable=False)


    def __str__(self):
        return(f"{self.first_name} {self.last_name}")


class Members(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    zone = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    crissingname = models.CharField(max_length=50)
    wereda = models.CharField(max_length=50)
    kebele = models.CharField(max_length=50)
    mothername= models.CharField(max_length=50)
    # foreign= User.ForeignKey(User.objects.all())
    #updatedAt = models.DateTimeField(default=timezone.now, editable=False)