from django.db.models import Q
from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from Messages.models import Message
from Messages.serializers import MessageSerializer

# Create your views here.


class MessageViewset(ModelViewSet):
    queryset = Message.objects
    permission_classes = [AllowAny]
    serializer_class = MessageSerializer

    def list(self, request, *args, **kwargs):
        data = self.request.query_params
        self.queryset = self.queryset.filter(
            Q(user1=data.get("user"), user2=data.get("user"))
        )

        response_data = self.serializer_class(self.queryset.all(), many=True)

        return Response(response_data.data)

        return super().list(request, *args, **kwargs)
