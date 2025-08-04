from django.urls import path
from . import views

app_name = "team"

urlpatterns = [
    path('', views.ListTeamView.as_view(), name="index"),
    path('create', views.CreateTeamView.as_view(), name="create"),
    path('<uuid:pk>/detail', views.DetailTeamView.as_view(), name="detail"),
    path('<uuid:pk>/edit', views.EditTeamView.as_view(), name="edit"),
]
