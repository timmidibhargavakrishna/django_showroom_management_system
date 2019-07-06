from django.db import models

# Create your models here.
class Bike(models.Model):
    bike_id = models.CharField(primary_key=True,max_length=15)
    bike_customer = models.CharField(max_length=50)
    bike_number = models.CharField(max_length=15)
    bike_type = models.CharField(max_length=50)
    bike_company = models.CharField(max_length=50)
    bike_description = models.CharField(max_length=500)
    #price = models.DecimalField(max_digits=10, decimal_places=2)
    #image = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.bike_id