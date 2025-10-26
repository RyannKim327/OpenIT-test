from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from Notifications.models import Notification
from Notifications.serializers import NotificationSerializer

# Create your views here.


class NotificationViewset(ModelViewSet):
    queryset = Notification.objects
    permission_classes = [AllowAny]
    serializer_class = NotificationSerializer

