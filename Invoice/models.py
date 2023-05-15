from django.db import models


# Create your models here.
class Payment(models.Model):
    payment_number = models.IntegerField()
    date = models.DateField()
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.CharField(max_length=255)
