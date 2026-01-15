from django.db import models
from manager.models import Client


# Create your models here.
class Trader(models.Model):

    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    email = models.EmailField()
    phone_number = models.IntegerField()
    password = models.CharField(max_length=255)
    promo_title = models.CharField(max_length=100)
    promo_content1 = models.TextField()
    promo_content2 = models.TextField()
    promo_content3 = models.TextField()


    def __str__(self):
        return self.user.email