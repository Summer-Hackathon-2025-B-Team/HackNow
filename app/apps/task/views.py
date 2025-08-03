from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from .models import Task

class ListTaskView(ListView):
    template_name = 'task/task_list.html'
    model = Task

# views.pyファイルの設定をします
class CreateTaskView(CreateView):
    template_name = 'task/task_create.html'
    model = Task
    # ブラウザ上で表示させる項目と記載します。
    fields = ('assignee', 'name', 'priority', 'start_date', 'end_date', 'status')

# DetailView(詳細表示ようのクラス)を継承して、DetailTaskViewという新しいビュークラスを定義している
class DetailTaskView(DetailView):
    # このビューが使うHTMLテンプレートはtask/task_detail.htmlです
    template_name = 'task/task_detail.html'
    # このビューで扱うデータはTaskモデルです
    model = Task
