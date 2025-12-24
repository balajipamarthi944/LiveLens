from django.db import models

# Create your models here.
class Offer(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    discount = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

