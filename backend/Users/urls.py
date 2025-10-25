from django.urls import include, path
from rest_framework.routers import SimpleRouter
from Users.viewsets.users import UserViewsets

routers = SimpleRouter()
routers.register(r"user", UserViewsets, basename="user")

urlpatterns = [path("", include(routers.urls))]
