from rest_framework import routers
from django.urls import path

from materials.views.lesson import LessonListView, LessonCreateView, LessonUpdateView, LessonDetailView, LessonDeleteView
from materials.views.course import CourseViewSet

router = routers.SimpleRouter()
router.register('course', CourseViewSet)

urlpatterns = [
                  path('', LessonListView.as_view(), name='lesson_list'),
                  path('create/', LessonCreateView.as_view(), name='lesson_create'),
                  path('lesson-update/<int:pk>/', LessonUpdateView.as_view(), name='lesson_update'),
                  path('lesson-info/<int:pk>/', LessonDetailView.as_view(), name='lesson_detail'),
                  path('lesson-delete/<int:pk>/', LessonDeleteView.as_view(), name='lesson_delete'),

              ] + router.urls
