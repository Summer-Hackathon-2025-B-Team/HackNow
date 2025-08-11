from django.db import models

# コース管理テーブル
class Past(models.Model):

    # 項目定義
    category = models.CharField(max_length=20, null=False, blank=False)
    name = models.CharField(max_length=30, null=False, blank=False)
    description = models.CharField(max_length=100, null=False, blank=False)
    url = models.URLField(max_length=255, null=False, blank=False)
    start_time = models.CharField(max_length=20, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        #明示的にテーブル名を指定（これをしないと、「アプリ名(小文字)_モデル名(小文字)」で自動命名される）
        db_table = 'past_apps'

    def __str__(self):
        return self.name
