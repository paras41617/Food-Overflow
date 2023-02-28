from django.db import models
from django.contrib.auth.models import User

class FoodProvider(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    description = models.TextField()
    quantity = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class FoodRecipient(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=20)

# class DonationRequest(models.Model):
#     donation = models.ForeignKey(FoodDonation, on_delete=models.CASCADE)
#     recipient = models.ForeignKey(FoodRecipient, on_delete=models.CASCADE)
#     date_requested = models.DateTimeField(auto_now_add=True)
