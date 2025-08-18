from django.db import models

# 参考情報管理テーブル
class Reference(models.Model):

    # 項目定義
    target = models.CharField(max_length=30, null=False, blank=False)
    content = models.TextField(max_length=255, null=False, blank=False)
    url = models.URLField(max_length=255, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        #明示的にテーブル名を指定（これをしないと、「アプリ名(小文字)_モデル名(小文字)」で自動命名される）
        db_table = 'references'
