import json

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(["GET"])
def intern_api_view(request):
        data = {
                "slackUsername": "izugance",
                "backend": True,
                "age": 20,
                "bio": ("I'm a young man who's enjoying his "
                        "wigglings through life's craziness."
                        )
                }
        return Response(data)