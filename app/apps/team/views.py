from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from .models import Team
from .forms import TeamForm

class ListTeamView(ListView):
    template_name = 'team/index.html'
    model = Team

    # 紐づくコース情報の最終発表日の降順（新しい日付が上）でソート 
    def get_queryset(self):
        return Team.objects.select_related("course").order_by("-course__last_report_date")

class CreateTeamView(CreateView):
    form_class = TeamForm
    template_name = 'team/create.html'
    model = Team
    success_url = reverse_lazy("team:index")

class DetailTeamView(DetailView):
    template_name = 'team/detail.html'
    model = Team

class EditTeamView(UpdateView):
    form_class = TeamForm
    template_name = 'team/edit.html'
    model = Team
    success_url = reverse_lazy("team:index")
