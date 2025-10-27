from django.db.models.signals import post_save
from django.dispatch import receiver
from Posts.models import Comment
from Notifications.models import Notification, UserNotification
from Users.models import User

@receiver(post_save, sender=Comment)
def new_comment(sender, instance, created,**kwargs):
    if not created:
        return

    post = instance.post
    commenter = instance.user
    

    notif = Notification.objects.create(
        content=f"New comment on {instance.comment_on_post.title}"
    )

    # get all the commenters (excluding or avoiding the one who commented)
    commenters = User.objects.filter(
        comments__post=post
    ).exclude(id=commenter.id).distinct()

    # Include post owner if they’re not the commenter
    if post.user != commenter:
        commenters = commenters.union(User.objects.filter(id=post.user.id))

    if not commenters.exists():
        return
    
    notif = Notification.objects.create(content=f"{commenter} also commented on {post.title}")

    for user in commenters:
        UserNotification.objects.create(user=user, notification=notif)




