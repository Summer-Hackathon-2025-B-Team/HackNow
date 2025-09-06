# Djangoのshortcuts(便利機能がまとめられたモジュール)からredirect(別のURLへリダイレクトするための関数)をインポートする。さらにデータベースからオブジェクトを取得し、見つからなけれあ404(エラーを返す関数)も一緒にインポートする
from django.shortcuts import redirect, get_object_or_404

from django.urls import reverse_lazy

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
)
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect

# 同じアプリ内の models.py から Document モデルを読み込む。
from .models import Document
# 同じアプリ内のforms.pyからDocumentFormフォームクラスを読み込む。
from .forms import DocumentForm

class DocumentListView(ListView):
    model = Document
    template_name = 'document/index.html'

    def get_queryset(self):
        """ログインユーザのチームの資料リンクのみ取得"""
        return Document.objects.filter(team=self.request.user.team).order_by('updated_at')

    def dispatch(self, request, *args, **kwargs):
        # ログインユーザがチーム未所属ならエラー画面にリダイレクト
        if request.user.team is None:
            return redirect('home:error') 
        return super().dispatch(request, *args, **kwargs)


class DocumentCreateView(CreateView):
    model = Document
    form_class = DocumentForm
    template_name = 'document/create.html'
    success_url = reverse_lazy('document:index')

    def form_valid(self, form):
        form.instance.team = self.request.user.team
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class DocumentUpdateView(UpdateView):
    model = Document
    template_name = 'document/edit.html'
    form_class = DocumentForm
    success_url = reverse_lazy('document:index')

    def form_valid(self, form):
        form.instance.team = self.request.user.team
        form.instance.created_by = self.request.user
        return super().form_valid(form)


# 資料リンク削除
@require_POST # 削除処理を POST 以外で叩けなくする
@csrf_protect # CSRF トークン必須にして外部からの POST を防ぐ
def delete_view(request, pk):
    # 該当レコードがなければ404エラーを返す
    document = get_object_or_404(Document, pk=pk)
    document.delete()
    return redirect('document:index')
