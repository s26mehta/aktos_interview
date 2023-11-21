from django.db import models

# Create your models here.
class ConsumerData(models.Model):
    id = models.IntegerField
    street = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    previous_jobs_count = models.IntegerField(default = 0)
    amount_due = models.CharField(max_length=20)
    lat = models.CharField(max_length=20)
    long = models.CharField(max_length=20)
