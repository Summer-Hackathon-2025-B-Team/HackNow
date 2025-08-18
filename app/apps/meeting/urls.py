from django.urls import path
from . import views

app_name = "meeting"

urlpatterns = [
    path('', views.ListMeetingView.as_view(), name="index"),
    path('create', views.CreateMeetingView.as_view(), name="create"),
    path('<int:pk>/edit', views.EditMeetingView.as_view(), name="edit"),
    path('<int:pk>/detail', views.DetailMeetingView.as_view(), name="detail"),
    path('<int:pk>/delete/', views.delete_meeting_view, name='delete'),
]
