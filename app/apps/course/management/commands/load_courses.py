from django.core.management.base import BaseCommand
from apps.course.models import Course

class Command(BaseCommand):
    help = 'コースデータを一括投入します'

    def handle(self, *args, **options):
        # コースデータ
        courses_data = [
            Course(id=1,name="2025春/基礎コース",interim_report_date="2025-5-10",last_report_date="2025-5-31",activity_status=False),
            Course(id=2,name="2025夏/チャレンジコース",interim_report_date="2025-8-9",last_report_date="2025-8-30",activity_status=True),
            Course(id=3,name="2025夏/基礎コース",interim_report_date="2025-8-9",last_report_date="2025-8-30",activity_status=True),
            Course(id=4,name="2025秋/基礎コース",interim_report_date="2025-11-8",last_report_date="2025-11-29",activity_status=False),
        ]

        try:
            # 既存データをクリア（必要に応じて）
            Course.objects.all().delete()

            # 一括投入実行
            Course.objects.bulk_create(courses_data, ignore_conflicts=True)

            self.stdout.write(
                self.style.SUCCESS(f'{len(courses_data)}件のコースデータを投入しました')
            )

        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'エラーが発生しました: {e}')
            )
