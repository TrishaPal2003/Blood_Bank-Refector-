from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from accounts.models import Account
from accounts.serializer import AccountSerializer


class AccountView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return Account.objects.get(user=self.request.user)
    
    def get(self, request, *args, **kwargs):
        account = self.get_object()
        serializer = AccountSerializer(account)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        account = self.get_objects()
        serializer = AccountSerializer(
            account,
            data = request.data,
            partial = False
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def fetch(self, request, *args, **kwargs):
        account = self.get_object()
        serializer = AccountSerializer(
            account,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)