from django.urls import path

from .views import intern_api_view

urlpatterns = [
    path('', intern_api_view)
]