from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import SignUpForm, LoginForm, AccountForm
from django.contrib.auth.views import LoginView as BaseLoginView, LogoutView as BaseLogoutView
from django.views.generic import UpdateView
from apps.user.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

# ユーザ登録
class SignupView(CreateView):
    form_class = SignUpForm
    template_name = "user/signup.html"

    # reverse_lazyはビューの定義時点でURLを解決するのではなく、遅延評価
    success_url = reverse_lazy("home:index")

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
