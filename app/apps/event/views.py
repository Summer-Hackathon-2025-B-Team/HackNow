from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Event
from .forms import EventForm
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect

class ListEventView(ListView):
    template_name = 'event/index.html'
    model = Event
    ordering = ["datetime"]

class CreateEventView(CreateView):
    form_class = EventForm
    template_name = 'event/create.html'
    model = Event
    success_url = reverse_lazy("event:index")

class EditEventView(UpdateView):
    form_class = EventForm
    template_name = 'event/edit.html'
    model = Event
    success_url = reverse_lazy("event:index")


# イベント削除
@require_POST # 削除処理を POST 以外で叩けなくする
@csrf_protect # CSRF トークン必須にして外部からの POST を防ぐ
def delete_view(request,pk):
    # 該当レコードがなければ404エラーを返す
    event = get_object_or_404(Event, pk=pk)
    event.delete()
    return redirect('event:index') 
