from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    )
from .models import Task
from .forms import TaskForm

class ListTaskView(ListView):
    template_name = 'task/index.html'
    model = Task

    def get_queryset(self):
        """ログインユーザのチームのタスクだけ取得"""
        return Task.objects.filter(team=self.request.user.team).order_by('end_date')


# views.pyファイルの設定をします
class CreateTaskView(CreateView):
    template_name = 'task/create.html'
    model = Task
    form_class = TaskForm
    # URLを指定する方法。reverse_lazyを使うと実際に画面上からrequestが来るタイミングまで関数が実行されない(lazy)ので、エラーにならずにクラス変数として定義でいる。
    success_url = reverse_lazy('task:index')

    def get_form_kwargs(self):
        """フォームにログインユーザを渡す"""
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        """保存前にteamを自動設定"""
        task = form.save(commit=False)
        task.team = task.assignee.team  # 担当者のteamを設定
        task.save()
        return super().form_valid(form)


class EditTaskView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task/edit.html'
    success_url = reverse_lazy('task:index')

    def get_form_kwargs(self):
        """フォームにログインユーザを渡す"""
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        """保存前にteamを自動設定"""
        task = form.save(commit=False)
        task.team = task.assignee.team  # 担当者のteamを設定
        task.save()
        return super().form_valid(form)


# タスク削除
def delete_view(request,pk):
    # 該当レコードがなければ404エラーを返す
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task:index') 
