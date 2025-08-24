import requests
from django.core.management.base import BaseCommand

WEBHOOK_URL = "https://chat.raretech.site/hooks/65fjaeaumjfs7ns5jhtuoae19h"

class Command(BaseCommand):
    help = 'Mattermostに通知を送信'

    def handle(self, *args, **kwargs):
        payload = {
            "text": "@all\ncronタスクトレース通知テスト\n「ゲイリーの散歩」が本日期限です。"
        }

        response = requests.post(WEBHOOK_URL, json=payload)

        if response.status_code == 200:
            self.stdout.write(self.style.SUCCESS('Mattermost通知完了'))
        else:
            self.stdout.write(self.style.ERROR(
                f'Mattermost通知失敗: {response.status_code} {response.text}'
            ))
