from rest_framework import status
from rest_framework.views import exception_handler


class CustomMixins:
    def handle_exception(self, exc):
        # TODO: To fairly check the user authorization
        response = exception_handler(exc, self.get_executed_handler_context())

        if (
            response is not None
            and response.status_code == status.HTTP_401_UNAUTHORIZED
        ):
            response = {
                "error": "Seems like your token is not valid, please try again."
            }
        return response
