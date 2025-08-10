from django.urls import path
from . import views

app_name = "past"

urlpatterns = [
    path('', views.ListPastView.as_view(), name="index"),
    path('create', views.CreatePastView.as_view(), name="create"),
    path('<int:pk>/edit', views.EditPastView.as_view(), name="edit"),
    path('<int:pk>/delete/', views.delete_view, name='delete'),
    path('api/items/', views.item_list_api, name='item_list_api'),
]
