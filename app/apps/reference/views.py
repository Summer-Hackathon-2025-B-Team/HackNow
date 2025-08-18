from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Reference
from .forms import ReferenceForm

class ReferenceListView(ListView):
    template_name = 'reference/index.html'
    model = Reference
    ordering = ["-id"]

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
def delete_view(request,pk):
    # 該当レコードがなければ404エラーを返す
    reference = get_object_or_404(Reference, pk=pk)
    reference.delete()
    return redirect('reference:index') 
