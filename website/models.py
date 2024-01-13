from datetime import timezone
from django.db import models

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
