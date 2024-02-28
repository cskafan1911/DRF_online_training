from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from materials.models import Course, Lesson
from subscriptions.models import Subscription
from users.models import User


class SubscriptionTestCase(APITestCase):
    """
    Тестирование модели Subscription.
    """

    def setUp(self) -> None:
        self.user = User.objects.create(
            email='test@test.ru',
            password='qwerty'
        )

        self.course = Course.objects.create(
            name='course_test',
            owner=self.user
        )

        self.lesson = Lesson.objects.create(
            name='lesson_test',
            course_lesson=self.course,
            owner=self.user
        )

        self.subscription = Subscription.objects.create(
            user=self.user,
            course=self.course,
        )

    def test_create_subscription(self):
        """
        Тестирование создания подписки
        """
        self.client.force_authenticate(user=self.user)

        data = {
            'user': self.user.id,
            'course': self.course.id,
        }
        response = self.client.post(
            reverse('subscriptions:subscription_create'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_list_subscription(self):
        """
        Тестирование списка подписок
        """
        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            reverse('subscriptions:subscription_list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_subscription(self):
        """Тестирование удаления подписок"""
        self.client.force_authenticate(user=self.user)

        response = self.client.delete(
            reverse('subscriptions:subscription_delete', args=[self.subscription.id])
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
