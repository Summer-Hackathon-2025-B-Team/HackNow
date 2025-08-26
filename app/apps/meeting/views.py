from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    )
from .models import Meeting
from apps.team.models import Team
from .forms import MeetingForm, AgendaFormSet
import requests
from django.contrib import messages
from django.utils import timezone


class ListMeetingView(ListView):
    template_name = 'meeting/index.html'
    model = Meeting

    def get_queryset(self):
        """ログインユーザのチームのミーティング情報だけ取得"""
        return Meeting.objects.filter(team=self.request.user.team).order_by('-datetime')

    def dispatch(self, request, *args, **kwargs):
        # ログインユーザがチーム未所属ならエラー画面にリダイレクト
        if request.user.team is None:
            return redirect('home:error') 
        return super().dispatch(request, *args, **kwargs)


# views.pyファイルの設定をします
class CreateMeetingView(CreateView):
    template_name = 'meeting/create.html'
    model = Meeting
    form_class = MeetingForm
    success_url = reverse_lazy('meeting:index')

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        formset = AgendaFormSet()
        return render(request, self.template_name, {"form": form, "formset": formset})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        formset = AgendaFormSet(request.POST)

        if form.is_valid() and formset.is_valid():

            # commit=FalseにすることでDBに保存しない（オブジェクト作成のみ実施）
            meeting = form.save(commit=False)

            # ログインユーザのteamを設定
            meeting.team = self.request.user.team

            # ここでDBに保存される
            meeting.save()

            agendas = formset.save(commit=False)
            for agenda in agendas:
                agenda.meeting = meeting
                agenda.save()
            return redirect('meeting:index') 
        
        return render(request, self.template_name, {"form": form, "formset": formset})


class EditMeetingView(UpdateView):

    model = Meeting
    form_class = MeetingForm
    template_name = 'meeting/edit.html'
    success_url = reverse_lazy('meeting:index')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['formset'] = AgendaFormSet(self.request.POST, instance=self.object)
        else:
            data['formset'] = AgendaFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        
        if form.is_valid() and formset.is_valid():
            meeting = form.save(commit=False)
            meeting.team = self.request.user.team
            meeting.save()

            agendas = formset.save(commit=False)
            for agenda in agendas:
                agenda.meeting = meeting
                agenda.save()

            # 削除対象の議題を削除
            for obj in formset.deleted_objects:
                obj.delete()

            return redirect('meeting:index')
        else:
            return self.render_to_response(self.get_context_data(form=form))


class DetailMeetingView(DetailView):
    template_name = 'meeting/detail.html'
    model = Meeting

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # 関連する議題（Agenda）を取得して追加
        context["agendas"] = self.object.agenda_set.all()

        return context


# ミーティング削除
def delete_meeting_view(request,pk):
    # 該当レコードがなければ404エラーを返す
    meeting = get_object_or_404(Meeting, pk=pk)
    meeting.delete()
    return redirect('meeting:index') 


# Mattermostへの通知
def notification_view(request,pk):

    meeting = get_object_or_404(Meeting, pk=pk)

    # ユーザが属するチームにMattermostのWebhookURLが設定されている場合
    if webhook_url := request.user.team.webhook_url: 

        # 日本時間に変換
        jst_datetime = timezone.localtime(meeting.datetime) 
        datetime = jst_datetime.strftime('%Y/%m/%d %H:%M')        
        message = "@all\n" + datetime + "実施分のミーティングについて議事内容を更新しました。\nご確認ください。"

        # Mattermostに送信
        mm_payload = {"text": message}
        mm_response = requests.post(webhook_url, json=mm_payload)
        messages.success(request, "議事更新通知をMattermostに通知しました。")
        return redirect('meeting:index') 

    messages.error(request, "MattermostのWebhookURLが未登録のため、議事更新通知ができませんでした。")
    return redirect('meeting:index') 
