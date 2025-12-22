from rest_framework import serializer
from users.models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializer.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        