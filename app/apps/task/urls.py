# Djangoのurlモジュールからpath関数を読み込む
from django.urls import path
# 同じ階層のディレクトリにあるviewsモジュールを読み込む . は現在のディレクトリ
from . import views

app_name = "task"

# DjangoがどのURLでどの処理(ビュー)を呼び出すかを判断するためのリスト
urlpatterns = [
  # トップページにアクセスされたら、タスク一覧を表示するListTaskViewを使って処理する。views.pyのreverse_lazy('list-task)が対応している。
  path('',views.ListTaskView.as_view(), name='index'),
  # /task_detail/ にアクセスされたとき、DetailTaskViewというビュークラスを呼び出す
  path('task/<int:pk>/detail/', views.DetailTaskView.as_view(), name='detail-task'),
  # URLがtask_create/の時、CreateTaskViewクラスのビューを呼び出す
  path('task_create/', views.CreateTaskView.as_view(), name='create-task'),
  # URLがtask/<init:pk>/delete/の時、DeleteTaskViewクラスのビューを呼び出す
  path('<int:pk>/delete/', views.DeleteTaskView.as_view(), name='delete-task'),
#
  path('<int:pk>/update/', views.UpdateTaskView.as_view(), name='update-task'),
]
