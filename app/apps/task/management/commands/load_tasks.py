from django.core.management.base import BaseCommand
from apps.task.models import Task
from apps.user.models import User
import uuid

user_id = uuid.UUID('ee9532c236e24d6fb8def03d3dbd8742')

class Command(BaseCommand):
    help = 'タスクデータを一括投入します'

    def handle(self, *args, **options):
        # タスクデータ
        tasks_data = [
            # Task(team='1', assignee=User.objects.get(pk=user_id), name="仕事", priority='2', start_date='2025-7-5', end_date='2025-7-20', status='3'),
            # Task(team='1', assignee=User.objects.get(pk=user_id), name="趣味", priority='3', start_date='2025-7-10', end_date='2025-7-31', status='2'),
            # Task(team='1', assignee=User.objects.get(pk=user_id), name="ハッカソン", priority='2', start_date='2025-8-1', end_date='2025-8-5', status='1'),
        ]

        try:
            # 既存データをクリア（必要に応じて）
            Task.objects.all().delete()

            # 一括投入実行
            Task.objects.bulk_create(tasks_data, ignore_conflicts=True)

            self.stdout.write(
                self.style.SUCCESS(f'{len(tasks_data)}件のタスクデータを投入しました')
            )

        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'エラーが発生しました: {e}')
            )
