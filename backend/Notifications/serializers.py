from rest_framework.serializers import Serializer
from Notifications.models import Notification

class NotificationSerializer(Serializer):
    class Meta:
        model = Notification
        fields = "__all__"

        