from BaseAuth.models import BaseAuthModel
from django.db import models
from Users.models import User

# Create your models here.


class Post(BaseAuthModel):
    order = "post_added"

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="post_as_user"
    )
    content = models.TextField()
    as_anonymous = models.BooleanField(default=False)
    post_added = models.DateTimeField(auto_now_add=True)


class Comment(BaseAuthModel):
    order = "comment_added"

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comment_as_user"
    )
    post = models.OneToOneField(
        Post, on_delete=models.CASCADE, related_name="comment_on_post"
    )
    content = models.CharField(max_length=1000)
    as_anonymous = models.BooleanField(default=False)
    comment_added = models.DateTimeField(auto_now_add=True)
