from django.contrib import auth
from django.db import models

User = auth.get_user_model()

class Customer(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15, blank=True)
    updated_by = models.CharField(max_length=100)
    updatedon = models.DateTimeField(auto_now_add=True)


class Address(models.Model):
    custome_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    addr_line1 = models.CharField(max_length=200)
    addr_line2 = models.CharField(max_length=200)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    updated_by = models.CharField(max_length=50)
    updatedon = models.DateTimeField(auto_now_add=True)
