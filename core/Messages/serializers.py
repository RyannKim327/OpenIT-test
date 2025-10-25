from rest_framework.serializers import Serializer

from Messages.model import Message


class MessageSerializer(Serializer):
    class Meta:
        model = Message
        fields = "__all__"
