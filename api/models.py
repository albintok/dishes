from asyncio.windows_events import NULL
from django.db import models


# Create your models here.
class Dishes(models.Model):
    name=models.CharField(max_length=100)
    catagory=models.CharField(max_length=100)
    image=models.ImageField(null=True,upload_to="pics")
    price=models.PositiveIntegerField()
    rating=models.PositiveIntegerField()

    def __str__(self):
        return self.name
