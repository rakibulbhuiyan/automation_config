from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('login', 'Login Done'),
        ('otp', 'OTP Verified'),
        ('reserved', 'Slot Reserved'),
        ('paid', 'Payment Done'),
        ('failed', 'Failed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=100)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    payment_url = models.TextField(null=True, blank=True)

    logs = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)