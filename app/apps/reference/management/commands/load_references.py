from django.core.management.base import BaseCommand
from apps.reference.models import Reference

class Command(BaseCommand):
    help = 'ハッカソン参考情報データを一括投入します'

    def handle(self, *args, **options):
        # ハッカソン参考情報データ
        references_data = [
            Reference(target="全体",content="ハッカソン概要",url="https://raretech.site/dashboard/hackathon"),
            Reference(target="全体",content="ハッカソン運営要領",url="https://var-inc.notion.site/RareTECH-f366cdf6c44c488dad019d56f738c316"),
            Reference(target="全体",content="ハッカソンTips",url="https://www.notion.so/var-inc/Tips-88ec3368f85a40f4a657306983365faf"),
            Reference(target="バックエンド",content="Django学習の参考書籍",url="https://www.amazon.co.jp/dp/479807392X/"),
            Reference(target="インフラ",content="Docker学習の参考記事",url="https://qiita.com/ikemura-ren/items/b961642d55e4e6515203"),
            Reference(target="インフラ",content="AWS学習の参考教材(Udemy)",url="https://www.udemy.com/course/aws-and-infra/?couponCode=LOCLZDOFFPJPCTRL"),
            Reference(target="入門コース",content="２週間以内に終わらせることリスト",url="https://var-inc.notion.site/df7c772815224feb8f8aa1721a9eac18"),
            Reference(target="全体",content="LiveShare（VSCodeの拡張機能）の参考記事",url="https://qiita.com/ibaryobaryo/items/e986b37da31cafc85ced"),
            Reference(target="全体",content="Git学習の参考記事",url="https://qiita.com/ikemura-ren/items/fe5082ad8ff8f626f5ee"),
            Reference(target="フロントエンド",content="デザイン基礎（動画）",url="https://www.youtube.com/watch?v=asXV-kuzlpY"),
            Reference(target="フロントエンド",content="Figmaの基本操作（動画）",url="https://www.youtube.com/watch?v=ad8KyRAazzg"),
        ]

        try:
            # 既存データをクリア（必要に応じて）
            Reference.objects.all().delete()

            # 一括投入実行
            Reference.objects.bulk_create(references_data, ignore_conflicts=True)

            self.stdout.write(
                self.style.SUCCESS(f'{len(references_data)}件のハッカソン参考情報データを投入しました')
            )

        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'エラーが発生しました: {e}')
            )
