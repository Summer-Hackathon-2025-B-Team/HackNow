from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from django import forms
from django.contrib.auth import authenticate

# カスタムユーザモデル用のユーザ登録フォーム
# UserCreationFormはパスワードの確認など、ユーザー作成に必要な機能を備えたフォーム
class SignUpForm(UserCreationForm):
    
    class Meta:
        # このフォームがUserモデルに基づいていることを示す
        model = User
        # フォームに含めるフィールドを指定
        fields = ('name', 'email', 'password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

       # nameフィールドにautofocusを追加（初期フォーカスが当たるようになる）
        self.fields['name'].widget.attrs.update({'autofocus': 'autofocus'})

        self.fields['name'].label = 'ユーザ名'
        self.fields['email'].label = 'メールアドレス'

        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

# ログインフォーム
class LoginForm(AuthenticationForm):

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        super().__init__(request, *args, **kwargs)
        self.fields['username'].label = 'メールアドレス'
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})

    def clean(self):
        email = self.cleaned_data.get('username') 
        password = self.cleaned_data.get('password')

        if email and password:
            self.user_cache = authenticate(self.request, username=email, password=password)
            if self.user_cache is None:
                raise forms.ValidationError("メールアドレスまたはパスワードが正しくありません")

            # is_active などのチェックを行う標準のメソッド
            self.confirm_login_allowed(self.user_cache)
        
        return self.cleaned_data
