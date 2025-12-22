from rest_framework import serializers
from requesters.models import Request
from users.serializer import UserSerializer

class RequesterSerializer(serializers.ModelSerializer):
    requester = UserSerializer(read_only = True)
    status = serializers.CharField(read_only = True) #always pending on creation
    
    class Meta:
        model = Request
        fields = '__all__'