from django.core.management.base import BaseCommand
from apps.task.models import Task
from apps.user.models import User
import uuid

user_id = uuid.UUID('09dca7b5c8ad4de69f45703901ed72a1')

class Command(BaseCommand):
    help = 'タスクデータを一括投入します'

    def handle(self, *args, **options):
        # タスクデータ
        tasks_data = [
            Task(team='1', assignee=User.objects.get(pk=user_id), name="要件定義", priority='2', start_date='2025-7-5', end_date='2025-7-20', status='3'),
            Task(team='1', assignee=User.objects.get(pk=user_id), name="テーブル設計", priority='3', start_date='2025-7-10', end_date='2025-7-31', status='2'),
            Task(team='1', assignee=User.objects.get(pk=user_id), name="ルート設計", priority='2', start_date='2025-8-1', end_date='2025-8-5', status='1'),
            Task(team='1', assignee=User.objects.get(pk=user_id), name="中間発表準備", priority='1', start_date='2025-8-4', end_date='2025-8-9', status='1'),
            Task(team='1', assignee=User.objects.get(pk=user_id), name="タスク管理機能の開発", priority='1', start_date='2025-7-31', end_date='2025-8-9', status='2'),
            Task(team='1', assignee=User.objects.get(pk=user_id), name="ER図作成",priority='1', start_date='2025-7-25', end_date='2025-7-31', status='3'),
        ]

        try:
            # 既存データをクリア（必要に応じて）
            # Task.objects.all().delete()

            # 一括投入実行
            Task.objects.bulk_create(tasks_data, ignore_conflicts=True)

            self.stdout.write(
                self.style.SUCCESS(f'{len(tasks_data)}件のタスクデータを投入しました')
            )

        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'エラーが発生しました: {e}')
            )
