from django.urls import path
from . import views

app_name = "course"

urlpatterns = [
    path('', views.ListCourseView.as_view(), name="index"),
    path('create', views.CreateCourseView.as_view(), name="create"),
]
