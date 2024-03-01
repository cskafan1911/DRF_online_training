from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from subscriptions.models import Subscription


@shared_task
def send_mail_for_subscriptions(pk):
    subscriptions = Subscription.objects.filter(course=pk)

    for subscription in subscriptions:
        course_name = subscription.course.name
        email = subscription.user.email

        send_mail(
            subject=f'Обновление курса {course_name}',
            message=f'Сообщаем что в курсе {course_name} произошли обновления.',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
        )
