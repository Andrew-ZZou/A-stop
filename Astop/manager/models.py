from django.db import models

# Create your models here.

class Client(models.Model):
    OCCUPATION_CHOICES = [('Plumber', 'Plumber'),
        ('Electrician', 'Electrician'),
        ('Handyman', 'Handyman'),]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100, choices=OCCUPATION_CHOICES)
    registration_code = models.CharField(max_length=100)
    trade_name = models.CharField(max_length=100)
    nzbn = models.CharField(max_length=100)

    def __str__(self):
        return self.user.email

