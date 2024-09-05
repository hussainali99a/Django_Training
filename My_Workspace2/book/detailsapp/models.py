from django.db import models

# Create your models here.
class Book(models.Model):
    bname = models.CharField(max_length=30)
    bprice = models.FloatField()
    
    def __str__(self):
        return self.bname

