from django.urls import path
from . import views

app_name = "event"

urlpatterns = [
    path('', views.ListEventView.as_view(), name="index"),
    path('create', views.CreateEventView.as_view(), name="create"),
    path('<int:pk>/edit', views.EditEventView.as_view(), name="edit"),
    path('<int:pk>/delete/', views.delete_view, name='delete'),
]
