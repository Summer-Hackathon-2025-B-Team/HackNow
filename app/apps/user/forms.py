from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from apps.team.models import Team
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
import uuid
from django.contrib.auth.password_validation import validate_password

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
        self.fields['name'].widget.attrs.update({
            'autofocus': 'autofocus',
            'autocomplete': 'nickname',
        })

        # emailフィールドにautocomplete=usernameを追加（ログイン時のIDがemailであることを明示）
        self.fields['email'].widget.attrs.update({
            'autocomplete': 'username',
        })

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

        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'メールアドレスを入力',
            'autocomplete': 'username',
        })

        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'パスワードを入力',
            'autocomplete': 'current-password',
        })

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

# ユーザ情報フォーム
class AccountForm(forms.ModelForm):

    password = forms.CharField(
        label='パスワード変更',
        required=False, # 未入力（パスワード変更なし）でもOK

        # <input type="password"> を使って「●●●」の見た目に        
        # render_value=False：フォーム初期表示時に中身を空にする
        widget=forms.PasswordInput(render_value=False), 
    )

    team_id_input = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'size': 40}),
    )

    class Meta:
        model = User
        fields = ('name', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # チームIDの初期値（既に設定があればそれを表示）
        if self.instance.team:
            self.fields['team_id_input'].initial = str(self.instance.team.id)

        # ラベルの設定
        self.fields['name'].label = 'ユーザ名'
     
        self.fields['password'].initial = ''

        self.fields['password'].widget.attrs.update({
            'placeholder': '変更したい場合に入力',
        })


    # チームIDチェック
    def clean_team_id_input(self):
        team_id = self.cleaned_data.get('team_id_input')
        if team_id:
            try:
                team_uuid = uuid.UUID(team_id)
                return Team.objects.get(id=team_uuid)  # 存在チェック
            except (ValueError, Team.DoesNotExist):
                raise forms.ValidationError("有効なチームIDではありません。")
        return None

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.team = self.cleaned_data.get('team_id_input')
        if commit:
            instance.save()
        return instance

    # パスワードチェック
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password:
            validate_password(password)  # 長さ・数字・記号などDjangoの基準でチェック
            return make_password(password)
        else:
            # 空欄の場合は元のパスワードをそのまま使う
            return self.instance.password

    # ユーザ名チェック
    def clean_name(self):
        username = self.cleaned_data.get('name')
    
        # すでに同じユーザ名を持つユーザが存在するかチェック
        same_name = User.objects.filter(name=username)

        # もし自分自身を編集しているなら、自分は除外
        if self.instance:
            same_name = same_name.exclude(pk=self.instance.pk)

        if same_name.exists():
            raise forms.ValidationError("既に登録されているユーザ名です。")

        return username
    