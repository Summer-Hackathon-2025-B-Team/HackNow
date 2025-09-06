from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Reference
from .forms import ReferenceForm
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect

class ReferenceListView(ListView):
    template_name = 'reference/index.html'
    model = Reference
    ordering = ["-id"]

    # ターゲットの選択肢を生成
    def get_target_choices(self):
        targets = Reference.objects.values_list('target', flat=True).distinct()
        return [('', 'すべて')] + [(c, c) for c in targets if c]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['targets'] = self.get_target_choices()
        return context


class ReferenceCreateView(CreateView):
    form_class = ReferenceForm
    template_name = 'reference/create.html'
    model = Reference
    success_url = reverse_lazy("reference:index")

class ReferenceEditView(UpdateView):
    form_class = ReferenceForm
    template_name = 'reference/edit.html'
    model = Reference
    success_url = reverse_lazy("reference:index")

# 参考情報の削除
@require_POST # 削除処理を POST 以外で叩けなくする
@csrf_protect # CSRF トークン必須にして外部からの POST を防ぐ
def delete_view(request,pk):
    # 該当レコードがなければ404エラーを返す
    reference = get_object_or_404(Reference, pk=pk)
    reference.delete()
    return redirect('reference:index') 



def target_filter_api(request):
    target = request.GET.get('target', '')
    items = Reference.objects.all()
    items = Reference.objects.all().order_by('-id')

    if target:
        items = items.filter(target=target)

    data = [
        {
            'target': item.target,
            'content': item.content,
            'url': item.url,
        }
        for item in items
    ]

    return JsonResponse({'items': data})
