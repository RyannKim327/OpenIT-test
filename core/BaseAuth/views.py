from BaseAuth.mixins import CustomMixins
from BaseAuth.paginator import BasicPaginator
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.


class BaseAuthViewset(ModelViewSet, CustomMixins):
    permission_classes = [IsAuthenticated]
    authenticated_classes = [JWTAuthentication]
    pagination_class = BasicPaginator

    def extract_error_handler(self, err):
        # TODO: To add an extractor for error handler
        if isinstance(err, dict):
            for key, value in err.items():
                if isinstance(value, list) and value:
                    return str(value[0])
                else:
                    return self.extract_error_handler(value)
        return str(err)
