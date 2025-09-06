from django.db import models

# イベント管理テーブル
class Event(models.Model):

    # 項目定義
    datetime = models.DateTimeField(null=True, blank=True,)
    title = models.CharField(max_length=30, null=True, blank=True)
    publish_status = models.BooleanField(default=True)
    detail_url = models.URLField(max_length=255, null=True, blank=True)
    zoom_url = models.URLField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        #明示的にテーブル名を指定（これをしないと、「アプリ名(小文字)_モデル名(小文字)」で自動命名される）
        db_table = 'events'

    def __str__(self):
        return self.name
