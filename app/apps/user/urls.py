from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path('', views.index_view, name="index"),
    path('signup/', views.SignupView.as_view(), name="signup"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('account/', views.UserEditView.as_view(), name="account"),
    path('<uuid:pk>/delete/', views.delete_view, name='delete'),
]
