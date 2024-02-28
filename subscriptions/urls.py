from django.urls import path

from subscriptions.apps import SubscriptionsConfig
from subscriptions.views import SubscriptionCreateAPIView, SubscriptionListAPIView, SubscriptionDeleteAPIView

app_name = SubscriptionsConfig.name

urlpatterns = [
    path('', SubscriptionListAPIView.as_view(), name='subscription_list'),
    path('create/', SubscriptionCreateAPIView.as_view(), name='subscription_create'),
    path('delete/<int:pk>/', SubscriptionDeleteAPIView.as_view(), name='subscription_delete'),

]
