from BaseAuth.models import BaseAuthModel
from django.db import models
from Users.models import User
# Create your models here.


class Notification(BaseAuthModel):
    order = "notification_added"
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="notifications"
    )
    content = models.CharField(max_length=80)
    read = models.BooleanField(default=False)
    notification_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{id}'
    