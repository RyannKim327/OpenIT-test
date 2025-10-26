from Posts.models import Comment, Post
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from Users.models import User
from Users.serializers import UserSerializer


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class PostSerializer(ModelSerializer):
    user_info = SerializerMethodField()

    class Meta:
        model = Post
        fields = "__all__"

    def get_user_info(self, obj):
        try:
            user = User.objects.get(id=obj.id)
            usr = UserSerializer(user)
            return usr.data
        except:
            pass

            