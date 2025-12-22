from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.serializer import UserSerializer

class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)