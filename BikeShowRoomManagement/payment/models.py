from django.db import models
# Create your models here.

class customer(models.Model):
    customer_id=models.CharField(max_length=10,primary_key=True)
    customer_name=models.CharField(max_length=20)
    customer_vehicle_name=models.CharField(max_length=20)
    customer_addres=models.TextField(max_length=200)
    customer_emi=models.CharField(max_length=10)
    customer_emi_palan=models.CharField(max_length=10)
    customer_done_payment=models.CharField(max_length=10)



class Payment(models.Model):
    payment_id = models.CharField(max_length=11,primary_key=True)
    payment_customer_id = models.CharField(max_length=11)
    payment_date = models.CharField(max_length=10)
    payment_bill = models.CharField(max_length=50)
    payment_type = models.CharField(max_length=8)
    payment_description = models.TextField(max_length=200)

    def __str__(self):
        return self.payment_type
