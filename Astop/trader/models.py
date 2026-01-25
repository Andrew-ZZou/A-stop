from django.db import models
from manager.models import Client


# Create your models here.
class Trader(models.Model):
    # client = models.OneToOneField(Client, on_delete=models.CASCADE)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE,db_column='client_id')
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    about_myself = models.TextField(null=True,blank=True)
    promo_title = models.CharField(max_length=100,null=True,blank=True)
    promo_content1 = models.TextField(null=True,blank=True)
    promo_content2 = models.TextField(null=True,blank=True)
    promo_content3 = models.TextField(null=True,blank=True)
    photo = models.ImageField(default='default_photo.png', upload_to='media/',null=True,blank=True)
    promo_image = models.ImageField(default='default_promo.png',upload_to='media/',null=True,blank=True)

    def __str__(self):
        return f"{self.client_id} - {self.email}"