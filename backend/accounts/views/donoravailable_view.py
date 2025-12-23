from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from accounts.models import Account
from accounts.serializer import AccountSerializer

class AvailableDonorListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        blood_group = request.query_params.get("blood_group")

        if not blood_group:
            return Response(
                {"detail": "Blood group is required"}, status=400
            )
        
        accounts = Account.objects.filter(
            blood_group = blood_group,
            is_available = True
        )

        eligible_accounts = [
            account for account in accounts if account.is_eligible()
        ]

        serializer = AccountSerializer(eligible_accounts, many= True)
        return Response(serializer.data)