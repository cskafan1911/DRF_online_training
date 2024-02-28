from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from materials.models import Course, Lesson
from subscriptions.models import Subscription
from users.models import User


class LessonTestCase(APITestCase):
    """
    Класс тестирования объектов Lesson.
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

    def test_create_lesson(self):
        """
        Тестирование создания урока.
        """
        self.client.force_authenticate(user=self.user)

        data = {
            'name': self.lesson.name,
            'course_lesson': self.course.id,
            'owner': self.user.id,
            'video_url': 'https://www.youtube.com/'
        }

        response = self.client.post(
            reverse('materials:lesson_create'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_list_lesson(self):
        """
        Тестирование вывода списка уроков.
        """
        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            reverse('materials:lesson_list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_detail_lesson(self):
        """
        Тестирование просмотра урока.
        """
        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            reverse('materials:lesson_detail', args=[self.lesson.id])
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_lesson(self):
        """
        Тестирование редактирования урока.
        """
        self.client.force_authenticate(user=self.user)

        data = {
            'name': 'TEST update',
            'course_lesson': self.course.id,
            'video_url': 'https://www.youtube.com/sdfsdfsgwergerg'
        }

        response = self.client.put(
            reverse('materials:lesson_update', args=[self.lesson.id]),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_lesson(self):
        """
        Тестирование удаления урока.
        """
        self.client.force_authenticate(user=self.user)

        response = self.client.delete(
            reverse('materials:lesson_delete', args=[self.lesson.id])
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
