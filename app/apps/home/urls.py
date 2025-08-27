from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path('', views.index_view, name='index'),
    path('error', views.error_view, name='error'),
    path('bonus', views.bonus_view, name='bonus'),
    path('opening', views.opening_view, name='opening'),
]
