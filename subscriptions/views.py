from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet

from materials.models import Course
from subscriptions.models import Subscription
from subscriptions.serializers import SubscriptionSerializer


class SubscriptionViewSet(ModelViewSet):
    """
    Контроллер для модели Subscription.
    """

    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
