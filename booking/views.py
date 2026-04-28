from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Booking
from worker.tasks import run_booking

class StartBooking(APIView):

    def post(self, request):
        booking = Booking.objects.create(
            user=request.user,
            phone=request.data['phone'],
            password=request.data['password']
        )

        run_booking.delay(booking.id)

        return Response({
            "message": "Booking started",
            "id": booking.id
        })