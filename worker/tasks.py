from celery import shared_task
from booking.services import IVACService

@shared_task(bind=True, max_retries=5)
def run_booking(self, booking_id):
    try:
        service = IVACService(booking_id)
        service.run()
    except Exception as e:
        raise self.retry(exc=e, countdown=10) 