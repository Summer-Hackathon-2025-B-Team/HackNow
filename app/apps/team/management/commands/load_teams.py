from django.core.management.base import BaseCommand
from apps.team.models import Team
import uuid

class Command(BaseCommand):
    help = 'チームデータを一括投入します'

    def handle(self, *args, **options):
        # チームデータ
        teams_data = [
            Team(id=uuid.UUID('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1'),course_id=2,name="Aチーム",webhook_url=""),
            Team(id=uuid.UUID('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa2'),course_id=3,name="Bチーム",webhook_url="https://chat.raretech.site/hooks/65fjaeaumjfs7ns5jhtuoae19h"),
            Team(id=uuid.UUID('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa3'),course_id=3,name="Cチーム",webhook_url=""),
            Team(id=uuid.UUID('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa4'),course_id=3,name="Dチーム",webhook_url=""),
            Team(id=uuid.UUID('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa5'),course_id=3,name="Eチーム",webhook_url=""),
            Team(id=uuid.UUID('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa6'),course_id=3,name="Fチーム",webhook_url=""),
            Team(id=uuid.UUID('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa7'),course_id=3,name="Gチーム",webhook_url=""),
        ]

        try:
            # 既存データをクリア（必要に応じて）
            #Team.objects.all().delete()

            # 一括投入実行
            Team.objects.bulk_create(teams_data, ignore_conflicts=True)

            self.stdout.write(
                self.style.SUCCESS(f'{len(teams_data)}件のチームデータを投入しました')
            )

        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'エラーが発生しました: {e}')
            )
