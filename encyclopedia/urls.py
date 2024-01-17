from django.urls import path

from . import views, util

app_name="encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>",views.entries,name="<str:name>"),
    path("wiki/",views.search,name="<str:name>"),
    path("get/",views.get_newpage,name="<str:name>"),
    path("get/<str:name>",views.get_edit, name="<str:name"),
    path("edit/<str:name>",views.edit_page,name="<str:name>")

]
