from django.core.management.base import BaseCommand
from apps.user.models import User

class Command(BaseCommand):
    help = 'ユーザデータを一括投入します'

    def handle(self, *args, **options):
        # ユーザデータ
        users_data = [
            User(name="管理者2ユーザ", password="kazu1222", email="admin2@gmail.com", is_active=1, is_staff=1),
        ]

        try:
            # 既存データをクリア（必要に応じて）
            # User.objects.all().delete()

            # 一括投入実行
            User.objects.bulk_create(users_data, ignore_conflicts=True)

            self.stdout.write(
                self.style.SUCCESS(f'{len(users_data)}件のタスクデータを投入しました')
            )

        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'エラーが発生しました: {e}')
            )
