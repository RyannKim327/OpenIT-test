from BaseAuth.views import BaseAuthViewset
from Posts.models import Post
from Posts.serializers import PostSerializer
from rest_framework.response import Response
from restframework.permission import AllowAny


class PostViewsets(BaseAuthViewset):
    permission_classes = [AllowAny]
    queryset = Post.objects
    serializer_class = PostSerializer

    def list(self, request, *args, **kwargs):
        page = self.paginate_queryset(self.queryset)

        if page:
            data = self.serializer_class(page, many=True)
            return self.get_paginated_response(data.data)

        data = self.serializer_class(self.queryset.all(), many=True)
        return Response(data.data)
