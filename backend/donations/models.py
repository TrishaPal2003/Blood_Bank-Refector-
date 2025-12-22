from django.db import models
from users.models import User
from requesters.models import Request
from .constant import Status
# Create your models here.

class Donation(models.Model):
    donor = models.ForeignKey(User, on_delete=models.CASCADE)
    request = models.ForeignKey(Request, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField()
    location = models.CharField()
    status = models.CharField(choices=Status, default="completed")
    created_at = models.DateTimeField(auto_now_add=True)

    def mark_completed(self):
        self.status = "completed"
        self.save()

    def __str__(self):
        return f"{self.donor.username} donated on {self.date}"