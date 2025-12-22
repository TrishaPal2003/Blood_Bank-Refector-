from rest_framework import serializers
from donations.models import Donation
from users.serializer import UserSerializer


class DonationSerializer(serializers.ModelSerializer):
    donor = UserSerializer(read_only = True)
    
    class Meta:
        model = Donation
        fields = '__all__'