from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from requesters.models import Request
from requesters.serializer import RequesterSerializer



class RequestStatusUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    ALLWOED_STATUSES = {"accepted", "rejected", "fulfilled"}

    def patch(self, request, request_id, *args, **kwargs):
        blood_request = get_object_or_404(request, pk=request_id)

        if not (request.user.is_staff or blood_request.requester == request.user):
            return Response(
                {"detail": "You don't have permission to update this request"}, status=status.HTTP_403_FORBIDDEN
            )
        new_status = request.data.get("stasus")

        if new_status not in self.ALLWOED_STATUSES:
            return Response(
                {"detail":{"invalid status value"}}, status=status.HTTP_400_BAD_REQUEST
            )
        if blood_request.status in {"fullfilled", "rejected"}:
            return Response(
                {"detail":"The request can no longer be updated"},status=status.HTTP_400_BAD_REQUEST
            )
        
        blood_request.status = new_status
        blood_request.save()

        serializer = RequesterSerializer(blood_request)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
            
        )