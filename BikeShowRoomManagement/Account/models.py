from django.db import models

# Create your models here.


class RegisterForm(models.Model):
    
    
    customer_id = models.CharField(primary_key=True,max_length=15)
    first_name=models.CharField(max_length = 30, blank = True)
    
    last_name=models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    address=models.CharField(max_length=50)
    joinng_date=models.CharField(max_length=10)
    phone_number = models.CharField(max_length=50)
