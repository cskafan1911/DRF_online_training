from rest_framework import serializers

from users.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    """
    Класс сериализатор для Payment.
    """

    class Meta:
        model = Payment
        fields = '__all__'
