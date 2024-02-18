from django.conf import settings
from django.db import models


class Course(models.Model):
    """
    Класс курса.
    """

    name = models.CharField(max_length=100, verbose_name='Название курса')
    photo = models.ImageField(upload_to='course_photo/', verbose_name='Фото', blank=True, null=True)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        """
        Строковое представление модели Course.
        """
        return f'{self.name}'

    class Meta:
        verbose_name = 'Курсы'
        verbose_name_plural = 'Курсы'
        ordering = ['name',]


class Lesson(models.Model):
    """
    Класс для урока.
    """

    name = models.CharField(max_length=100, verbose_name='Название урока')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    photo = models.ImageField(upload_to='lesson_photo', verbose_name='Фото', blank=True, null=True)
    video_url = models.URLField(verbose_name='Ссылка на видео', blank=True, null=True)

    course_lesson = models.ForeignKey(Course, on_delete=models.SET_NULL, related_name='course_lesson',
                                      verbose_name='Курс', null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        """
        Строковое представление модели Lesson.
        """
        return f'{self.name}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ['name', 'course_lesson',]
