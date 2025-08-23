# Djangoのモデル機能を使うためのインポート。models
from django.db import models

# apps/team/models.pyに定義されているTeamクラスを、このファイルで使えるようにする
from apps.team.models import Team

# ユーザモデルの取得
from django.contrib.auth import get_user_model
User = get_user_model()

# 資料リンク管理テーブル
class Document(models.Model):

    # 項目定義

    # チームID（チーム管理テーブルの外部キー）必須入力であり、対応するユーザが削除されたらこのレコードも連動して削除されます
    team = models.ForeignKey(Team, null=False, blank=False, on_delete=models.CASCADE)

    # 作成者 (ユーザーモデルを参照する外部キー)必須入力であり、対応するユーザが削除されたらこのレコードも連動して削除されます
    created_by = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)

    # 資料名
    name = models.CharField(max_length=30, null=False, blank=False)

    # 資料リンクURL
    url = models.URLField(max_length=255, null=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        #明示的にテーブル名を指定（これをしないと、「アプリ名(小文字)_モデル名(小文字)」で自動命名される）
        db_table = 'documents'

        # データベースからこのモデルのレコードを取得する時のデフォルトの並び順を指定します。
        ordering = ["-updated_at"]

        # データベースに複数インデックスを作ります。インデックスデータ検索の高速化。第1キーはteam列、第2キーはupdated_at列の降順
        indexes = [
            models.Index(fields=["team", "-updated_at"]),
            ]

    # Documentオブジェクトを文字列に変換するとき、資料名を返す
    def __str__(self):
        return self.name
