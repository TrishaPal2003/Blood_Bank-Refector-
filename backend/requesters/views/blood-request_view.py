from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from requesters.serializer import RequesterSerializer




class CreateBloodRequestView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = RequesterSerializer(
            data = request.data,
            context = {"request": request}
        )

        serializer.is_valid(raise_exception=True)
        # blood_request = serializer.save(requester = request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)