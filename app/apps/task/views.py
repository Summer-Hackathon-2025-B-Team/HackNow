from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    DeleteView,
    UpdateView,
    )
from .models import Task
from .forms import TaskForm

class ListTaskView(ListView):
    template_name = 'task/task_list.html'
    model = Task

# views.pyファイルの設定をします
class CreateTaskView(CreateView):
    template_name = 'task/task_create.html'
    model = Task
    # form_class = TaskForm
    fields = ['assignee', 'name', 'priority', 'start_date', 'end_date', 'status']
    # URLを指定する方法。reverse_lazyを使うと実際に画面上からrequestが来るタイミングまで関数が実行されない(lazy)ので、エラーにならずにクラス変数として定義でいる。
    success_url = reverse_lazy('task:index')

# DetailView(詳細表示ようのクラス)を継承して、DetailTaskViewという新しいビュークラスを定義している
class DetailTaskView(DetailView):
    # このビューが使うHTMLテンプレートはtask/task_detail.htmlです
    template_name = 'task/task_detail.html'
    # このビューで扱うデータはTaskモデルです
    model = Task

# DeleteView（Djangoが提供する汎用ビュー）を継承して、新しいDeleteTaskViewというクラスを定義しています
class DeleteTaskView(DeleteView):
    # このビューが操作の体操とするモデル(データベーステーブル)はTaskだという指定です。結果URLで指定されたTaskのIDに対応するレコードを削除対象として扱います
    model = Task
    # 削除確認のために表示するテンプレート(HTMLファイル)のパスを指定しています
    template_name = 'task/task_confirm_delete.html'
    # 成功後、指定されたlist-taskから実際のURLパスを遅延評価で取得します
    success_url = reverse_lazy('task:index')


class UpdateTaskView(UpdateView):
    model = Task
    # form_class = TaskForm
    fields = ['assignee', 'name', 'priority', 'start_date', 'end_date', 'status']
    template_name = 'task/task_update.html'
    success_url = reverse_lazy('task:index')
