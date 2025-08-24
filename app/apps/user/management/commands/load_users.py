from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from apps.user.models import User
from apps.team.models import Team
import uuid

hashpass = make_password("password")

class Command(BaseCommand):
    help = 'ユーザデータを一括投入します'

    def handle(self, *args, **options):
        # ユーザデータ
        users_data = [
            User(name="ハッカソン運営ユーザ",email="admin@gmail.com",password=hashpass,is_active=True,is_staff=True),
            User(team=Team.objects.get(pk=uuid.UUID('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1')),name="ARISA@45期",email="a1@gmail.com",password=hashpass,is_active=True,is_staff=False),
            User(team=Team.objects.get(pk=uuid.UUID('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1')),name="honda@41期",email="a2@gmail.com",password=hashpass,is_active=True,is_staff=False),
            User(team=Team.objects.get(pk=uuid.UUID('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1')),name="ぽんず@48期",email="a3@gmail.com",password=hashpass,is_active=True,is_staff=False),
            User(team=Team.objects.get(pk=uuid.UUID('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1')),name="りょうけん@46期",email="a4@gmail.com",password=hashpass,is_active=True,is_staff=False),
            User(team=Team.objects.get(pk=uuid.UUID('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1')),name="ふじ@42期",email="a5@gmail.com",password=hashpass,is_active=True,is_staff=False),
            User(team=Team.objects.get(pk=uuid.UUID('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa2')),name="サンディ@54期",email="b1@gmail.com",password=hashpass,is_active=True,is_staff=False),
            User(team=Team.objects.get(pk=uuid.UUID('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa2')),name="とよふく@52期",email="b2@gmail.com",password=hashpass,is_active=True,is_staff=False),
            User(team=Team.objects.get(pk=uuid.UUID('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa2')),name="ゆーせー@53期",email="b3@gmail.com",password=hashpass,is_active=True,is_staff=False),
            User(team=Team.objects.get(pk=uuid.UUID('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa3')),name="ちえ@56期",email="c1@gmail.com",password=hashpass,is_active=True,is_staff=False),
            User(team=Team.objects.get(pk=uuid.UUID('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa3')),name="ちかこ@53期",email="c2@gmail.com",password=hashpass,is_active=True,is_staff=False),
            User(team=Team.objects.get(pk=uuid.UUID('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa3')),name="トイトイ@55期",email="c3@gmail.com",password=hashpass,is_active=True,is_staff=False),
            User(team=Team.objects.get(pk=uuid.UUID('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa3')),name="なそにゅ@54期",email="c4@gmail.com",password=hashpass,is_active=True,is_staff=False),
            User(team=Team.objects.get(pk=uuid.UUID('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa4')),name="MANA@44期",email="d1@gmail.com",password=hashpass,is_active=True,is_staff=False),
            User(team=Team.objects.get(pk=uuid.UUID('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa4')),name="たな@53期",email="d2@gmail.com",password=hashpass,is_active=True,is_staff=False),
            User(team=Team.objects.get(pk=uuid.UUID('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa4')),name="てつき@51期",email="d3@gmail.com",password=hashpass,is_active=True,is_staff=False),
            User(team=Team.objects.get(pk=uuid.UUID('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa4')),name="ひいろ@52期",email="d4@gmail.com",password=hashpass,is_active=True,is_staff=False),
            User(team=Team.objects.get(pk=uuid.UUID('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa5')),name="えめっと@42期",email="e1@gmail.com",password=hashpass,is_active=True,is_staff=False),
            User(team=Team.objects.get(pk=uuid.UUID('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa5')),name="こうた@49期",email="e2@gmail.com",password=hashpass,is_active=True,is_staff=False),
            User(team=Team.objects.get(pk=uuid.UUID('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa5')),name="そそぎ@48期",email="e3@gmail.com",password=hashpass,is_active=True,is_staff=False),
            User(team=Team.objects.get(pk=uuid.UUID('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa5')),name="ちか@54期",email="e4@gmail.com",password=hashpass,is_active=True,is_staff=False),
            User(team=Team.objects.get(pk=uuid.UUID('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa6')),name="masa@45期",email="f1@gmail.com",password=hashpass,is_active=True,is_staff=False),
            User(team=Team.objects.get(pk=uuid.UUID('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa6')),name="やましん@56期",email="f2@gmail.com",password=hashpass,is_active=True,is_staff=False),
            User(team=Team.objects.get(pk=uuid.UUID('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa6')),name="リョウ@52期",email="f3@gmail.com",password=hashpass,is_active=True,is_staff=False),
            User(team=Team.objects.get(pk=uuid.UUID('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa6')),name="なおき@45期",email="f4@gmail.com",password=hashpass,is_active=True,is_staff=False),
            User(team=Team.objects.get(pk=uuid.UUID('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa7')),name="こうすけ@48期",email="g1@gmail.com",password=hashpass,is_active=True,is_staff=False),
            User(team=Team.objects.get(pk=uuid.UUID('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa7')),name="なお@47期",email="g2@gmail.com",password=hashpass,is_active=True,is_staff=False),
            User(team=Team.objects.get(pk=uuid.UUID('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa7')),name="まい@51期",email="g3@gmail.com",password=hashpass,is_active=True,is_staff=False),
            User(team=Team.objects.get(pk=uuid.UUID('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa7')),name="Ryo@46期",email="g4@gmail.com",password=hashpass,is_active=True,is_staff=False),
        ]

        try:
            # 既存データをクリア（必要に応じて）
            User.objects.all().delete()

            # 一括投入実行
            User.objects.bulk_create(users_data, ignore_conflicts=True)

            self.stdout.write(
                self.style.SUCCESS(f'{len(users_data)}件のユーザデータを投入しました')
            )

        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'エラーが発生しました: {e}')
            )
