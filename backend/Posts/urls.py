from django.urls import include, path
from Posts.viewsets.posts import PostViewsets
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r"posts", PostViewsets, basename="posts")

urlpatterns = [path("", include(router.urls))]
