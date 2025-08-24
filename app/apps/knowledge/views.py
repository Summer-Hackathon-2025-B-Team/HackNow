from django.shortcuts import redirect, get_object_or_404
# Djangoのreverse_lazy関数を読み込む。URLパターン名から実際のURL文字列を遅延的に逆引き（＝クラス定義時にまだURLが読み込まれていなくても使える）するための関数。
from django.urls import reverse_lazy
# Djangoの汎用クラスベースビュー（ListView/DetailView/CreateView/UpdateView/DeleteView）を読み込む。それぞれ一覧・詳細・作成・更新・削除の画面を簡単に作るためのビュークラス。
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
)

# 同じアプリ内の models.py から Knowledge モデルを読み込む。
from .models import Knowledge
# 同じアプリ内のforms.pyからKnowledgeFormフォームクラスを読み込む。
from .forms import KnowledgeForm

class KnowledgeListView(ListView):
        
    model = Knowledge
    template_name = 'knowledge/index.html'

    def get_queryset(self):
        """ログインユーザのチームのナレッジのみ取得（更新日が新しいものを上に）"""
        return Knowledge.objects.filter(team=self.request.user.team).order_by('updated_at')

    def dispatch(self, request, *args, **kwargs):
        # ログインユーザがチーム未所属ならエラー画面にリダイレクト
        if request.user.team is None:
            return redirect('home:error') 
        return super().dispatch(request, *args, **kwargs)

class KnowledgeCreateView(CreateView):
    model = Knowledge
    form_class = KnowledgeForm
    template_name = 'knowledge/create.html'
    success_url = reverse_lazy('knowledge:index')

    def form_valid(self, form):
        form.instance.team = self.request.user.team
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class KnowledgeUpdateView(UpdateView):
    model = Knowledge
    template_name = 'knowledge/edit.html'
    form_class = KnowledgeForm
    success_url = reverse_lazy('knowledge:index')

    def form_valid(self, form):
        form.instance.team = self.request.user.team
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class KnowledgeDetailView(DetailView):
    template_name = 'knowledge/detail.html'
    model = Knowledge
    

# タスク削除
def delete_view(request,pk):
    # 該当レコードがなければ404エラーを返す
    knowledge = get_object_or_404(Knowledge, pk=pk)
    knowledge.delete()
    return redirect('knowledge:index') 
