from BaseAuth.models import BaseAuthModel
from django.db import models
from Users.models import User

# Create your models here.


class Message(BaseAuthModel):
    order = "date_added"

    user1 = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="messages_for_user1"
    )
    user2 = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="messages_for_user2"
    )
    message = models.CharField(max_length=150)
    is_anon = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{id}"
