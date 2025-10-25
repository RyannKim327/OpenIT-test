from rest_framework.serializers import ModelSerializer

from system.Posts.models import Comment, Post


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
