from django.db import models
from django.conf import settings

from materials.models import Course


class Subscription(models.Model):
    """
    Класс для модели подписка.
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    course = models.ForeignKey(
        Course, on_delete=models.SET_NULL, related_name='subscription_course',
        verbose_name='Подписка', null=True
    )

    def __str__(self):
        """
        Строковое представление модели Subscription.
        """
        return f'{self.course.name}'

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
    