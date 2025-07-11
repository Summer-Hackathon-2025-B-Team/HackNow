# docker/Dockerfile

FROM python:3.10-slim

# 作業ディレクトリ作成
WORKDIR /app

# 依存ファイルをコピー
COPY ../requirements.txt ./

# 必要なOSパッケージとPythonパッケージをインストール
RUN apt-get update && \
    apt-get install -y default-libmysqlclient-dev gcc && \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# volume
EXPOSE 8000

