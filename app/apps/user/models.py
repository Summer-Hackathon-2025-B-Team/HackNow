from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import uuid

# カスタムユーザのマネージャークラス（ユーザ作成用のロジックを提供）
class UserManager(BaseUserManager):

    # ユーザ作成の共通処理（内部利用用）
    def _create_user(self, name, email, password, **extra_fields):
        if not name:
            raise ValueError('名前は必須です')
        if not email:
            raise ValueError('メールアドレスは必須です')
        if not password:
            raise ValueError("パスワードは必須です。")

        # 大文字などを正規化
        email = self.normalize_email(email)

        # ユーザインスタンスの作成
        user = self.model(name=name, email=email,  **extra_fields)

        # パスワードのハッシュ化
        user.set_password(password)

        user.save()
        return user

    # 一般ユーザの作成
    def create_user(self, name, email, password, **extra_fields):

        # 管理者フラグ（is_staff）と全権限フラグ（is_superuser）をFalseに
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        # _create_user を内部的に呼び出し
        return self._create_user(name, email, password, **extra_fields)

    # スーパーユーザ（管理者）の作成
    def create_superuser(self, name, email, password, **extra_fields):

        # 管理者フラグ（is_staff）と全権限フラグ（is_superuser）をTrueに
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        # _create_user を内部的に呼び出し
        return self._create_user(name, email, password, **extra_fields)


# カスタムユーザーモデル
class User(AbstractBaseUser, PermissionsMixin):

    # 主キー定義（uuid.uuid4:新規作成時にランダムなUUID（v4）を自動生成、editable=False:管理画面やフォームで手入力不可（自動生成専用））
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # 項目定義
    # 【備忘】team_idはチーム管理テーブル作成後、外部キーにすること！
    team_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=20, null=False, blank=False, unique=True)
    email = models.EmailField(max_length=50, null=False, blank=False, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    # ログイン時のユーザー識別に使うフィールド(メールアドレスをIDにする)
    USERNAME_FIELD = 'email'

    # スーパーユーザー作成時（createsuperuser）に必須の追加フィールド
    REQUIRED_FIELDS = ['name']

    class Meta:
        #明示的にテーブル名を指定（これをしないと、「アプリ名(小文字)_モデル名(小文字)」で自動命名される）
        db_table = 'users'
        swappable = 'AUTH_USER_MODEL'

    # クリーンメソッド（保存前処理）
    def clean(self):
        super().clean()
