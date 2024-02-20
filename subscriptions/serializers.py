from rest_framework import serializers

from subscriptions.models import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):
    """
    Класс сериализатор для модели Subscription.
    """

    class Meta:
        model = Subscription
        fields = '__all__'
