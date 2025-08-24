from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Past
from .forms import PastForm
from django.http import JsonResponse

class ListPastView(ListView):
    template_name = 'past/index.html'
    model = Past
    ordering = ["-id"]

    # カテゴリの選択肢を生成
    def get_category_choices(self):
        categories = Past.objects.values_list('category', flat=True).distinct()
        return [('', 'すべてのカテゴリ')] + [(c, c) for c in categories if c]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = self.get_category_choices()
        return context

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


def category_filter_api(request):
    category = request.GET.get('category', '')
    items = Past.objects.all()
    items = Past.objects.all().order_by('-id')

    if category:
        items = items.filter(category=category)

    data = [
        {
            'category': item.category,
            'name': item.name,
            'description': item.description,
            'url': item.url,
            'start_time': item.start_time
        }
        for item in items
    ]

    return JsonResponse({'items': data})

# タスク削除
def delete_view(request,pk):
    # 該当レコードがなければ404エラーを返す
    past_app = get_object_or_404(Past, pk=pk)
    past_app.delete()
    return redirect('past:index') 
