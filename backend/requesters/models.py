from django.db import models
import uuid
from users.models import User
from accounts.constant import Blood_Group_Choices
from .constant import Status

# Create your models here.

class Request(models.Model):
    requester = models.ForeignKey(User, on_delete=models.CASCADE)
    blood_group = models.CharField(choices=Blood_Group_Choices, max_length=3)
    location = models.TextField()
    status = models.CharField(choices=Status, max_length=20)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def mark_fulfilled(self):
        self.status = "fulfilled"
        self.save()

    @classmethod
    def filter_by_blood_group(cls, bg):
        return cls.objects.filter(blood_group = bg, status="pending")
