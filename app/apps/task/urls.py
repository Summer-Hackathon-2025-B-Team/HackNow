# Djangoのurlモジュールからpath関数を読み込む
from django.urls import path
# 同じ階層のディレクトリにあるviewsモジュールを読み込む . は現在のディレクトリ
from . import views

app_name = "task"

# DjangoがどのURLでどの処理(ビュー)を呼び出すかを判断するためのリスト
urlpatterns = [
  # トップページにアクセスされたら、タスク一覧を表示するListTaskViewを使って処理する。views.pyのreverse_lazy('list-task)が対応している。
  path('',views.ListTaskView.as_view(), name='index'),
  # URLがtask_create/の時、CreateTaskViewクラスのビューを呼び出す
  path('create/', views.CreateTaskView.as_view(), name='create'),
  path('<int:pk>/edit/', views.EditTaskView.as_view(), name='edit'),
  path('<int:pk>/delete/', views.delete_view, name='delete'),
]
