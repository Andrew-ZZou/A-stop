from django.db import models

# Create your models here.

class Client(models.Model):
    OCCUPATION_CHOICES = [('Plumber', 'Plumber'),
        ('Electrician', 'Electrician'),
        ('Handyman', 'Handyman'),]
    client_id = models.CharField(max_length=10,unique=True,primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100, choices=OCCUPATION_CHOICES)
    registration_code = models.CharField(max_length=100)
    trade_name = models.CharField(max_length=100)
    nzbn = models.CharField(max_length=100)

    def __str__(self):
        return self.user.email
# set client id auto increase as format of C****
    def save(self, *args, **kwargs):
        if not self.client_id:
            last = Client.objects.all().order_by('client_id').last()
            if last:
                last_number = int(last.client_id[1:])
                new_number = last_number + 1
            else:
                new_number = 1

            self.client_id = f"C{new_number:04d}"

        super(Client,self).save(*args, **kwargs)
