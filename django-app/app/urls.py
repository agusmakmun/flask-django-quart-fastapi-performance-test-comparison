from django.urls import path
from app.views import dummy_view

urlpatterns = [
    path("api/dummy", dummy_view, name="dummy"),
]
