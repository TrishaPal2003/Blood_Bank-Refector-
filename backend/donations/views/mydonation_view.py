from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from donations.models import Donation
from donations.serializer import DonationSerializer


class MyDonationView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        donations = Donation.objects.filter(donor = request.user).order_by('-created_at')
        serializer = DonationSerializer(Donation, many = True)
        return Response(serializer.data)