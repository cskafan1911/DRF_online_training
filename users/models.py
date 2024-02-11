from django.contrib.auth.models import AbstractUser
from django.db import models

from config.settings import AUTH_USER_MODEL
from materials.models import Course, Lesson


class User(AbstractUser):
    """
    Класс пользователя.
    """

    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    phone = models.CharField(max_length=15, verbose_name='Телефон', blank=True, null=True)
    city = models.CharField(max_length=100, verbose_name='Город', blank=True, null=True)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Payment(models.Model):
    """
    Класс для платежей.
    """

    CASH = 'Наличные'
    CARD = 'Перевод'
    PAYMENT_METHOD = [
        (CASH, 'Наличные'),
        (CARD, 'Перевод')
    ]

    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_payment')
    date_of_payment = models.DateTimeField(verbose_name='Дата платежа', auto_now=True)
    payment_amount = models.DecimalField(verbose_name='Сумма оплаты', max_digits=9, decimal_places=2, blank=True,
                                         null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='payment_of_course', blank=True,
                               null=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='payment_of_lesson', blank=True,
                               null=True)
    method = models.CharField(max_length=100, verbose_name='Способ оплаты', choices=PAYMENT_METHOD, default=CARD,
                              blank=True, null=True)

    def __str__(self):
        """
        Строковое представление класса Payment.
        """
        return f'{self.user} - {self.method}: {self.payment_amount}'

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
