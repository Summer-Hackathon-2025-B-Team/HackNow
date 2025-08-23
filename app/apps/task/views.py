from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    )
from .models import Task
from .forms import TaskForm
from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import requests


class ListTaskView(ListView):
    template_name = 'task/index.html'
    model = Task

    def get_queryset(self):
        """ログインユーザのチームのタスクだけ取得"""
        return Task.objects.filter(team=self.request.user.team).order_by('end_date')

    def dispatch(self, request, *args, **kwargs):
        # ログインユーザがチーム未所属ならエラー画面にリダイレクト
        if request.user.team is None:
            return redirect('home:error') 
        return super().dispatch(request, *args, **kwargs)


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


def gantt_view(request):
    tasks = Task.objects.filter(
        team=request.user.team,
        status__in=[1, 2]
    )

    data = []
    for t in tasks:
        data.append({
            "id": t.id,            
            "name": t.name,
            "assignee": t.assignee.name,
            "assignee_id": t.assignee.id,
            "start": t.start_date.strftime("%Y-%m-%d"),
            "end": t.end_date.strftime("%Y-%m-%d"),
        })
    return JsonResponse(data, safe=False)


# 当日期限・期限切れタスク通知（Lambdaからの呼び出しを想定）
@csrf_exempt
@require_POST
def notify_expired_tasks_view(request):

    today = timezone.localdate()  

    # 当日期限タスク
    due_today_tasks = Task.objects.filter(
        end_date=today,
        status__in=[1, 2]
    ).select_related("team")

    # 期限切れタスク（今日より前のタスク）　※__lt は "less than"（より小さい） という意味
    overdue_tasks = Task.objects.filter(
        end_date__lt=today,
        status__in=[1, 2]
    ).select_related("team")

    results = []
    for task in due_today_tasks:
        webhook_url = ""
        webhook_url = task.team.webhook_url
        if webhook_url:
            payload = {
                "text": f"@all\n"
                        f"**＜テスト送信：本日期限のタスク＞**\n"
                        f"- タスク名: {task.name}\n"
                        f"- 担当者: {task.assignee}\n"
                        f"- 終了予定日: {task.end_date}\n"
            }
            r = requests.post(webhook_url, json=payload)
            results.append({"task": task.name, "status": r.status_code})

    for task in overdue_tasks:
        webhook_url = ""
        webhook_url = task.team.webhook_url
        if webhook_url:
            payload = {
                "text": f"@all\n"
                        f"**＜テスト送信：期限切れタスク＞**\n"
                        f"- タスク名: {task.name}\n"
                        f"- 担当者: {task.assignee}\n"
                        f"- 終了予定日: {task.end_date}\n"
            }
            r = requests.post(webhook_url, json=payload)
            results.append({"task": task.name, "status": r.status_code})

    return JsonResponse({"count": len(results), "results": results})
