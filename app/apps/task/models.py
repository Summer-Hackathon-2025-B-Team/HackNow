# Djangoのモデル機能を使うためのインポート。models.
from django.db import models
# from django.conf import settings

# ユーザモデルの取得
from django.contrib.auth import get_user_model
User = get_user_model()

# チーム管理モデルの取得
# from apps.team.models import Team


# class Task(models.Model):
#     STATUS_CHOICES = [
#         (0, '未着手'),
#         (1, '進行中'),
#         (2, '完了'),
#     ]
# class Priority(models.IntegerChoices):
#     HIGH = 3, '高'
#     MEDIUM = 2, '中'
#     LOW = 1, '低'


# 優先度の選択肢を定義
PRIORITY_CHOICES = (
    (1,"高"),
    (2,"中"),
    (3,"低"),
)

# ステータスの選択肢を定義
STATUS_CHOICES = (
    (1,"未着手"),
    (2,"対応中"),
    (3,"完了"),
)

# Taskモデルの定義
# Taskと言う名前のモデル(データベーステーブル)を定義します。このモデルはDjangoのmodels.Modelを継承しており、DjangoのORMで管理されるテーブルになります。
class Task(models.Model):

    # 【備忘】team_idはチーム管理テーブル作成後、外部キーにすること！
    team = models.IntegerField(null=True, blank=True)

    # settings.pyで AUTH_USER_MODEL = 'user.User' としている

    # 担当者ID（ユーザテーブルの外部キー）
    assignee = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=20,null=False, blank=False,)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, null=False, blank=False,)
    start_date = models.DateField(null=False, blank=False,)
    end_date = models.DateField(null=False, blank=False,)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1, null=False, blank=False,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        # 明示的にテーブル名を指定（これをしないと、「アプリ名(小文字)_モデル名(小文字)」で自動命名される)この指定をしないと、task_taskになります
        db_table = 'tasks'
