from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import SignUpForm, LoginForm, AccountForm
from django.contrib.auth.views import LoginView as BaseLoginView, LogoutView as BaseLogoutView
from django.views.generic import UpdateView
from apps.user.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect

# ユーザ一覧
def index_view(request):

    # ユーザテーブルから全ユーザ取得(作成日時の降順)
    users = User.objects.all().order_by('-created_at')
    return render(request, 'user/index.html', {'users': users})


# ユーザ登録
class SignupView(CreateView):
    form_class = SignUpForm
    template_name = "user/signup.html"

    # reverse_lazyはビューの定義時点でURLを解決するのではなく、遅延評価
    success_url = reverse_lazy("home:opening")

    # フォームのバリデーションが問題ない時に実行
    def form_valid(self, form):
        response = super().form_valid(form)
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password1")

        # 入力されたemailとpasswordを元に認証チェック
        user = authenticate(self.request, email=email, password=password)
        if user is not None:
            # 問題なければログイン状態にする
            login(self.request, user)
        return response

# ログイン
class LoginView(BaseLoginView):
    form_class = LoginForm
    template_name = "user/login.html"

# ログアウト
class LogoutView(BaseLogoutView):
    success_url = reverse_lazy("user:login")

# ユーザ情報
class UserEditView(UpdateView):
    form_class = AccountForm
    template_name = 'user/account.html'
    model = User
    success_url = reverse_lazy("home:index")

    def get_object(self):
        return self.request.user  # 自分の情報を更新

    # パスワード変更後もセッションを維持
    def form_valid(self, form):
        response = super().form_valid(form)
        update_session_auth_hash(self.request, self.object) 
        messages.success(self.request, "ユーザ情報を更新しました")
        return response

# ユーザ削除
@require_POST # 削除処理を POST 以外で叩けなくする
@csrf_protect # CSRF トークン必須にして外部からの POST を防ぐ
def delete_view(request,pk):
    # 該当レコードがなければ404エラーを返す
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return redirect('user:index') 
