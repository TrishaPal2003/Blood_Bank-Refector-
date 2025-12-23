from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser


from donations.models import Donation
from donations.serializer import DonationSerializer

class AllDonationView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, *args, **kwargs):
        donations = Donation.objects.all().order_by("-created_at")
        serializer = DonationSerializer(donations, many=True)
        return Response(serializer.data)