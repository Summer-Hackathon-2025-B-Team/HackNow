from django.db import models
# apps/team/models.pyに定義されているTeamクラスを、このファイルで使えるようにする
from apps.team.models import Team

# Djangoはmodel.Modelを継承してモデルを定義すると、主キーidカラムは自動で追加されます。
class Knowledge(models.Model):
    # チーム(UUID主キーのTeamを外部キーで参照)
    team = models.ForeignKey(Team, null=False, blank=False, on_delete=models.CASCADE)
    # タイトル
    title = models.CharField(max_length=30, null=False, blank=False)
    # 複数行・長文なので、TextField
    content = models.CharField(max_length=255, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'knowledges'
        # データベースからこのモデルのレコードを取得する時のデフォルトの並び順を指定します。
        ordering = ['-updated_at']
        # データベースに複数インデックスを作ります。インデックスデータ検索の高速化。第1キーはteam列、第2キーはupdated_at列の降順
        indexes = [ models.Index(fields=['item', '-updated_at']), ]

    # 管理画面やシェルでオブジェクトを文字列化した時にどう表示するかを指定します。
    def __str__(self):
        return self.title
