from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework import status
from accounts.models import Account
from accounts.serializer import AccountSerializer
from django.shortcuts import get_object_or_404


class AccountDetailView(APIView):
    permission_classes = [IsAdminUser]

    
    def get_object(self, account_id):
        return get_object_or_404(Account, pk=account_id)

    #read
    def get(self, request, account_id, *args, **kwargs):
        account = self.get_object(account_id)
        serializer = AccountSerializer(account)
        return Response(serializer.data)
    
    #update(Full)
    def put(self, request, account_id, *args, **kwargs):
        account = self.get_object(account_id)
        serializer = AccountSerializer(account, data=request.data)
        serializer.is_valid(raise_excception= True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    #update(partial)
    def patch(self, request, account_id, *args, **kwargs):
        account = self.get_object(account_id)
        serializer = AccountSerializer(account, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    #delete
    def delete(self, request, account_id, *args, **kwargs):
        account = self.get_object(account_id)
        account.delete()
        return Response(
            {"detail": "Account deleted successfully."},
            status=status.HTTP_204_NO_CONTENT
        )

    
