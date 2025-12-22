from rest_framework import serializers
from notifications.models import Notification
from users.serializer import UserSerializer
from requesters.serializer import RequestSerializer
from donations.serializer import DonationSerializer

class NotificationSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    receiver = UserSerializer(read_only=True)
    request = RequestSerializer(read_only=True)
    donation = DonationSerializer(read_only=True)
    created_at = serializers.ReadOnlyField()

    class Meta:
        model = Notification
        fields = [
            'notification_id',
            'sender',
            'receiver',
            'request',
            'donation',
            'title',
            'message',
            'notification_type',
            'is_read',
            'created_at',
        ]
        read_only_fields = [
            'notification_id',
            'sender',
            'receiver',
            'request',
            'donation',
            'created_at',
        ]
