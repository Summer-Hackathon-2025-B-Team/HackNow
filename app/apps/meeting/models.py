from django.db import models
from apps.team.models import Team

# ミーティング管理テーブル
class Meeting(models.Model):

    # 項目定義

    # チームID（チーム管理テーブルの外部キー）
    team = models.ForeignKey(Team, null=False, blank=False, on_delete=models.CASCADE)

    # 実施日時
    datetime = models.DateTimeField(null=False, blank=False,)

    # ミーティング名
    name = models.CharField(max_length=30, null=False, blank=False)

    # 持ち帰り事項
    homework = models.TextField(max_length=255, null=True, blank=True)

    # 次回ミーティング日時
    next_datetime = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        #明示的にテーブル名を指定（これをしないと、「アプリ名(小文字)_モデル名(小文字)」で自動命名される）
        db_table = 'meetings'

# 議題管理テーブル
class Agenda(models.Model):

    # 項目定義

    # ミーティングID（外部キー）
    meeting = models.ForeignKey(Meeting, null=False, blank=False, on_delete=models.CASCADE)

    # 議題名
    name = models.CharField(max_length=30, null=False, blank=False)

    # 議事内容
    content = models.TextField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        #明示的にテーブル名を指定（これをしないと、「アプリ名(小文字)_モデル名(小文字)」で自動命名される）
        db_table = 'agendas'
