# Djangoのurlモジュール(config/urls.py)からpath関数を読み込む
from django.urls import path

# 同じ階層のディレクトリにあるviewsモジュールを読み込む . は現在のディレクトリ
from . import views

# このアプリ（document）のURLパターンには document: という接頭辞をつけて区別します
app_name = 'document'

urlpatterns = [
    # /document/にアクセスしたときにマッチするようにURLとビューを対応づける。name='index'このURLパターンに「index」と言う名前をつける。
    path('', views.DocumentListView.as_view(), name='index'),
    path('create/', views.DocumentCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', views.DocumentUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', views.delete_view, name='delete'),
]
