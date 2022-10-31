from django.urls import path

from .views import InternApiView

urlpatterns = [
    path('', InternApiView.as_view())
]