from django.urls import path
import re
from . import views

urlpatterns = [
#    path("wiki", views.index, name="index"),
    path("<str:entries>", views.index, name="articals")
]
