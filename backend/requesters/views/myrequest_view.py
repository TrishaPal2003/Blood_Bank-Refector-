from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from requesters.serializer import RequesterSerializer
from requesters.models import Request


class MyRequestView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        requests = Request.objects.filter(requester = request.user)
        serializer = RequesterSerializer(requests, many=True)
        return Response(serializer.data)