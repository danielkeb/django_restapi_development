from django.db import models

class Drinks(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.name} {self.description}"
