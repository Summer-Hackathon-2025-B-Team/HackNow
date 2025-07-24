from django.contrib.auth.forms import UserCreationForm
from .models import User

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

        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
