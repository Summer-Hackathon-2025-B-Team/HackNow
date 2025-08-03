from django.db import models

# コース管理テーブル
class Course(models.Model):

    # 項目定義
    name = models.CharField(max_length=20, null=False, blank=False, unique=True)
    Interim_report_date = models.DateField(null=False, blank=False)
    last_report_date = models.DateField(null=False, blank=False)
    activity_status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        #明示的にテーブル名を指定（これをしないと、「アプリ名(小文字)_モデル名(小文字)」で自動命名される）
        db_table = 'courses'

    def __str__(self):
        return self.name
