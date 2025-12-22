from rest_framework import serializers
from accounts.models import Account
from users.serializer import UserSerializer

class AccountSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True) 
    is_eligible = serializers.ReadOnlyField()

    class Meta:
        model = Account
        fields = '__all__'