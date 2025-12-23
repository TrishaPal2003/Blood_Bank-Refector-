from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from requesters.models import Request
from requesters.serializer import RequesterSerializer


class AllRequestView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, *args, **kwargs):
        requests = Request.objects.all().order_by('-created_at')
        serializer = RequesterSerializer(requests, many = True)
        return Response(serializer.data)
    
    
