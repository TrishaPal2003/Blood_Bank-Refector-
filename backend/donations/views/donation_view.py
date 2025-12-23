from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.utils import timezone

from donations.models import Donation
from donations.serializer import DonationSerializer
from requesters.models import Request
from accounts.models import Account


class DonationView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, request_id, *args, **kwargs):
        blood_request = get_object_or_404(Request, pk=request_id)

        if Donation.objects.filter(donor = request.user, request=blood_request).exists():
            return Response(
                {"detail": "you have already donatedd for this request"}, status=status.HTTP_400_BAD_REQUEST
            )
        
        donation = Donation.objects.create( 
            donor = request.user,
            request = blood_request
        )

        account = get_object_or_404(Account, user=request.user)
        account.last_donation_date = timezone.now().date()
        account.is_available = False
        account.save()

        if blood_request.status != "fulfilled":
            blood_request.status = "fulfilled"
            blood_request.save()

        serializer = DonationSerializer(donation)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

