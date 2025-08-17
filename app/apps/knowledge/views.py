# Djangoの認証システムが提供する「ログインしているユーザーしかアクセスできないようにする」ためのMixinクラス LoginRequiredMixin を読み込む
from django.contrib.auth.mixins import LoginRequiredMixin
# Djangoのreverse_lazy関数を読み込む。URLパターン名から実際のURL文字列を遅延的に逆引き（＝クラス定義時にまだURLが読み込まれていなくても使える）するための関数。
from django.urls import reverse_lazy
# Djangoの汎用クラスベースビュー（ListView/DetailView/CreateView/UpdateView/DeleteView）を読み込む。それぞれ一覧・詳細・作成・更新・削除の画面を簡単に作るためのビュークラス。
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

# 同じアプリ内の models.py から Knowledge モデルを読み込む。
from .models import Knowledge
# 同じアプリ内のforms.pyからKnowledgeFormフォームクラスを読み込む。
from .forms import KnowledgeForm

# 「ログインしていないユーザーはログインページにリダイレクトする」機能を追加。
class TeamQuerysetMixin(LoginRequiredMixin):
    # 常に自分のチームのレコードだけを見る 更新日の降順。
    def get_queryset(self):
        return Knowledge.objects.filter(team=self.request.user.team).order_by('-updated_at')

class KnowledgeListView(TeamQuerysetMixin, ListView):
    model = Knowledge
    template_name = 'knowledge/index.html'
    context_object_name = 'items'

class KnowledgeDetailView(TeamQuerysetMixin, DetailView):
    model = Knowledge
    template_name = 'knowledge/detail.html'
    context_object_name = 'item'

class KnowledgeCreateView(TeamQuerysetMixin, CreateView):
    model = Knowledge
    form_class = KnowledgeForm
    template_name = 'knowledge/create.html'
    success_url = reverse_lazy('knowledge:index')
    def form_valid(self, form):
        form.instance.team = self.request.user.team
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class KnowledgeUpdateView(TeamQuerysetMixin, UpdateView):
    model = Knowledge
    template_name = 'knowledge/edit.html'
    form_class = KnowledgeForm
    success_url = reverse_lazy('knowledge:index')

class KnowledgeDeleteView(TeamQuerysetMixin, DeleteView):
    model = Knowledge
    template_name = 'knowledge/delete.html'
    success_url = reverse_lazy('knowledge:index')

    # def get_queryset(self):
    # # チーム内かつ自分が作成者のものだけ削除対象
    # return super().get_queryset().filter(created_by=self.request.user)
