from django.db.models.signals import post_save
from django.dispatch import receiver
from Posts.models import Comment
from Notifications.models import Notification


@receiver(post_save, sender=Comment)
def new_comment(sender, instance, created,**kwargs):
    if not created:
        return

    user = instance.comment_as_user
    poster = instance.comment_on_post.user
    
    # avoid notifying the poster when he comments on his own post
    if user == poster:
        return

    Notification.objects.create(
        user=poster,
        content=f'{user.middle_name} commented on your post "{instance.comment_on_post.title}"'
    )


