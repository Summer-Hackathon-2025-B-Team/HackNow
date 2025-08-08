from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Past
from .forms import PastForm
from django.http import JsonResponse

class ListPastView(ListView):
    template_name = 'past/index.html'
    model = Past
    ordering = ["-id"]

class CreatePastView(CreateView):
    form_class = PastForm
    template_name = 'past/create.html'
    model = Past
    success_url = reverse_lazy("past:index")

class EditPastView(UpdateView):
    form_class = PastForm
    template_name = 'past/edit.html'
    model = Past
    success_url = reverse_lazy("past:index")

# カテゴリでの非同期フィルタ
def category_filter(request):

    category = request.GET.get('category')

    if category:
        past_apps = Past.objects.filter(category=category)
    else:
        past_apps = Past.objects.all()

    data = {'past_apps': [
        {
            'category': Past.category, 
        }for past_app in past_apps
    ]}

    return JsonResponse(data)
