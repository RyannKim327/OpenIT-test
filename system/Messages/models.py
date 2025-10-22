from django.db import models

from Users.models import User

# Create your models here.


class Message(models.Model):
    user1 = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="messages_user1"
    )
    user2 = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="messages_user2"
    )
    message = models.CharField(max_length=150)
    is_anon = models.BooleanField(default=False)

    def __str__(self):
        return f"{id}"
