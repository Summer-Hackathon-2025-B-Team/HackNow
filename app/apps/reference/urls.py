from django.urls import path
from . import views

app_name = "reference"

urlpatterns = [
    path('', views.ReferenceListView.as_view(), name="index"),
    path('create', views.ReferenceCreateView.as_view(), name="create"),
    path('<int:pk>/edit', views.ReferenceEditView.as_view(), name="edit"),
    path('<int:pk>/delete/', views.delete_view, name='delete'),
]
