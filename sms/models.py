from django.db import models

# Create your models here.
class Sms(models.Model):
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.phone_number