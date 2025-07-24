from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import SignUpForm
from .models import User

# ユーザ登録
class SignupView(CreateView):
    form_class = SignUpForm
    template_name = "user/signup.html"

    # reverse_lazyはビューの定義時点でURLを解決するのではなく、遅延評価
    success_url = reverse_lazy("user:signup")

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
