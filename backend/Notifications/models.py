from BaseAuth.models import BaseAuthModel
from django.db import models
from Users.models import User
# Create your models here.


class Notification(BaseAuthModel):
    order = "notification_added"
    content = models.CharField(max_length=80)
    notification_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{id}'
    
# added through model for per-user read status hahahaha
# this let us trach each users read status
class UserNotification(BaseAuthModel):
    order = "read_at"

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_notification')
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE)
    read = models.BooleanField(default=False)
    read_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        unique_together = ('user','notification')

    def __str__(self):
        return f'{id}'