from django.db import models

class MenuItem(models.Model):
    dish_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.dish_name

class Order(models.Model):
    cus_name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=6, decimal_places=2,default=0.00)
    order_status = models.CharField(max_length=10)
    def __str__(self):
        return self.cus_name