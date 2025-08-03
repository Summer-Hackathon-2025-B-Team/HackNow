# Djangoのurlモジュールからpath関数を読み込む
from django.urls import path
# 同じ階層のディレクトリにあるviewsモジュールを読み込む . は現在のディレクトリ
from . import views

# DjangoがどのURLでどの処理(ビュー)を呼び出すかを判断するためのリスト
urlpatterns = [
  # トップページにアクセスされたら、タスク一覧を表示するListTaskViewを使って処理する
  path('',views.ListTaskView.as_view()),
  # /task_detail/ にアクセスされたとき、DetailTaskViewというビュークラスを呼び出す
  path('task/<int:pk>/detail/', views.DetailTaskView.as_view()),
  # URLがtask_create_の時、CreateTaskViewクラスのビューを呼び出す
  path('task_create_', views. CreateTaskView.as_view()),
]
