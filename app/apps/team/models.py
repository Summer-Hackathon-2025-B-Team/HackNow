from django.db import models
from apps.course.models import Course
import uuid

# チーム管理テーブル
class Team(models.Model):

    # 項目定義

    # チームID（主キー）：uuidで定義
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    # コースID（外部キー）
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    # チーム名
    name = models.CharField(max_length=10, null=False, blank=False)

    # webhookのURL
    webhook_url = models.URLField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        #明示的にテーブル名を指定（これをしないと、「アプリ名(小文字)_モデル名(小文字)」で自動命名される）
        db_table = 'teams'
