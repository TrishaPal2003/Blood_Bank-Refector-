from django.db import models

# Create your models here.

import uuid
from .constant import Blood_Group_Choices
from users.models import User
from django.utils import timezone

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    blood_group = models.CharField(choices=Blood_Group_Choices, max_length=3)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    last_donation_date = models.DateField(null=True, blank=True)
    is_available = models.BooleanField(default=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_eligible(self):
        if not self.last_donation_date:
            return True
        return (timezone.now().date() - self.last_donation_date).days >= 90