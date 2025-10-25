from BaseAuth.views import BaseAuthViewset
from django.contrib.auth import authenticate
from django.db.models import Q
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.routers import Response
from rest_framework_simplejwt.tokens import RefreshToken
from Users.models import User
from Users.serializers import UserSerializer


class UserViewsets(BaseAuthViewset):
    queryset = User.objects.filter()
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    @action(
        detail=False, url_path="login", permission_classes=[AllowAny], methods=["POST"]
    )
    def login(self, request):
        data = request.data
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return Response({"error": "Please provide username or password"})

        try:
            user = self.queryset.get(
                Q(username=username, email=username) | Q(password=password)
            )
        except:
            return Response({"error": "Invalid credentials"})

        usr = authenticate(username=user.username, password=password)

        if not usr:
            return Response({"error": "Invalid Credentals"})
        refresh = RefreshToken.for_user(usr)

        return Response(
            {
                "message": "User logged in",
                "refresh": refresh,
                "access": str(refresh.access_token),
                "user": {
                    "username": usr.username,
                    "first_name": usr.first_name,
                    "middle_name": usr.middle_name,
                    "last_name": usr.last_name,
                    "email": usr.email,
                },
            }
        )

    @action(
        detail=False,
        url_path="register",
        permission_classes=[AllowAny],
        methods=["POST"],
    )
    def register(self, request):
        data = request.data
        try:
            serialize = self.serializer_class(data=data, partial=True)
            if serialize.is_valid():
                user = serialize.save()
                user.set_password(data["password"])

                return Response({"message": "Account created successfully."})
            return Response({"error": self.extract_error_handler(serialize.error)})
        except Exception as e:
            return Response({"error": str(e)})
