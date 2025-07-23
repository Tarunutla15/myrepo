from django.urls import path
from .views import show_my_name

urlpatterns = [
    path("",show_my_name, name="show_my_name"),
]
