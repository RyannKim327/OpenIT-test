from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainSerializer(TokenPairSerializer):
    @classmethod
    def get_token(self, usr):
        token = super().get_token(usr)

        token["is_superuser"] = usr.is_superuser
        token["username"] = usr.username
        token["groups"] = list(usr.groups.values_list("name", flat=True))
        return token
