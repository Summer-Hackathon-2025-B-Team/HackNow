# /app/gunicorn.conf.py

import multiprocessing

# バインド先 (Nginx 経由なので 0.0.0.0:8000)
bind = "0.0.0.0:8000"

# ワーカー数: CPUコア数 * 2 + 1 が目安
workers = multiprocessing.cpu_count() * 2 + 1

# スレッド数 (必要なら)
threads = 2

# タイムアウト（秒）長すぎるとゾンビプロセスが残る
timeout = 30

# アプリのエントリーポイント
wsgi_app = "config.wsgi:application"

# アクセスログを標準出力に
accesslog = "-"
errorlog = "-"
loglevel = "info"

# graceful reload 対応
graceful_timeout = 30

