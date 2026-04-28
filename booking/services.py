# booking/services.py

from core.http import HttpClient
from .models import Booking

http = HttpClient()

class IVACService:

    def __init__(self, booking_id):
        self.booking = Booking.objects.get(id=booking_id)

    def log(self, msg):
        self.booking.logs += msg + "\n"
        self.booking.save()

    def login(self):
        self.log("Logging in...")
        # এখানে তোমার script login logic বসাও
        self.booking.status = "login"
        self.booking.save()

    def verify_otp(self):
        self.log("Verifying OTP...")
        self.booking.status = "otp"
        self.booking.save()

    def reserve(self):
        self.log("Reserving slot...")
        self.booking.status = "reserved"
        self.booking.save()

    def payment(self):
        self.log("Generating payment...")
        self.booking.payment_url = "https://payment-url.com"
        self.booking.status = "paid"
        self.booking.save()

    def run(self):
        try:
            self.login()
            self.verify_otp()
            self.reserve()
            self.payment()
        except Exception as e:
            self.booking.status = "failed"
            self.log(str(e))
            self.booking.save()