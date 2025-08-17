from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    )
from .models import Meeting
from .forms import MeetingForm, AgendaFormSet

class ListMeetingView(ListView):
    template_name = 'meeting/index.html'
    model = Meeting

    def get_queryset(self):
        """ログインユーザのチームのミーティング情報だけ取得"""
        return Meeting.objects.filter(team=self.request.user.team).order_by('datetime')


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
