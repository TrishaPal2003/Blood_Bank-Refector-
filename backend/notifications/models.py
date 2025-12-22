from django.db import models
import uuid
from users.models import User
from requesters.models import Request
from donations.models import Donation
from .constant import Notification_Type
# Create your models here.

class Notification(models.Model):
    notification_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_notifications")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_notifications")
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    message = models.TextField()
    notification_type = models.CharField(choices=Notification_Type, max_length=50)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification to {self.receiver.username}: {self.title}"
