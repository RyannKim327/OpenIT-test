from BaseAuth.views import BaseAuthViewset
from Posts.models import Post
from Posts.serializers import PostSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


class PostViewsets(BaseAuthViewset):
    permission_classes = [AllowAny]
    queryset = Post.objects
    serializer_class = PostSerializer

    def list(self, request, *args, **kwargs):
        page = self.paginate_queryset(self.queryset.filter())

        if page:
            data = self.serializer_class(page, many=True)
            return self.get_paginated_response({"data": data.data})

        data = self.serializer_class(self.queryset.all(), many=True)
        return Response(data.data)
