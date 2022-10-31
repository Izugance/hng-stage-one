from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class InternApiView(APIView):
    def get(self, request, *args, **kwargs):
        """Return a data response in the specified format."""
        data = {
                "slackUsername": "izugance",
                "backend": True,
                "age": 20,
                "bio": ("I'm a young man who's enjoying his "
                        "wigglings through life's craziness."
                        )
                }

        return Response(data, status=status.HTTP_200_OK)

