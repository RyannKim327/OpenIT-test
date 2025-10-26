from django.urls import include, path
from Notifications.views import NotificationViewset
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r"notifications",NotificationViewset, basename="notifications")


urlpatterns = [
    path("", include(router.urls))
]
