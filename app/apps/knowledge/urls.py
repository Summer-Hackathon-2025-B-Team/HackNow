# Djangoのurlモジュール(config/urls.py)からpath関数を読み込む
from django.urls import path
# 同じ階層のディレクトリにあるviewsモジュールを読み込む . は現在のディレクトリ
from . import views

app_name = 'knowledge'

# DjangoがどのURLでどの処理(ビュー)を呼び出すかを判断するためのリスト
urlpatterns = [
    path('', views.KnowledgeListView.as_view(), name='index'),
    path('create/', views.KnowledgeCreateView.as_view(), name='create'),
    path('<int:pk>/detail', views.KnowledgeDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', views.KnowledgeUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', views.delete_view, name='delete'),
]
