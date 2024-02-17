from django.db import models

# Create your models here.
class emp(models.Model):
    name = models.CharField(max_length = 200)
    empId = models.CharField(max_length = 200)
    Phone = models.CharField(max_length = 10)
    address = models.CharField(max_length = 150)
    working = models.BooleanField(default = True)
    department = models.CharField(max_length = 10)