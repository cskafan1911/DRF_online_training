from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from materials.models import Course
from subscriptions.models import Subscription
from subscriptions.serializers import SubscriptionSerializer


class SubscriptionCreateAPIView(CreateAPIView):
    """
    Контроллер для создания объекта модели Subscription.
    """

    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data
        course_item = get_object_or_404(Course, pk=course_id.get('course'))
        subs_item = Subscription.objects.filter(user=user, course=course_item)

        if subs_item.exists():
            subs_item.delete()
            subs_item.create(user=user, course=course_item, is_subscribed=course_id.get('is_subscribed'))
            message = 'Подписка удалена'
        else:
            subs_item.create(user=user, course=course_item, is_subscribed=course_id.get('is_subscribed'))
            message = 'Подписка сохранена'

        return Response({'message': message})


class SubscriptionListAPIView(ListAPIView):
    """
    Контроллер для просмотра подписок.
    """

    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Subscription.objects.filter(user=self.request.user)


class SubscriptionDeleteAPIView(DestroyAPIView):
    """
    Класс для удаления подписки.
    """

    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated]
