# docker/Dockerfile

FROM python:3.10-slim

# 作業ディレクトリ作成
WORKDIR /app

# wait-for-it.shをコンテナにコピー
COPY ./docker/wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

# 依存ファイルをコピー
COPY requirements.txt ./

# 必要なOSパッケージとPythonパッケージをインストール
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
	build-essential \
	pkg-config \
	default-libmysqlclient-dev \ 
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# アプリ本体をコピー
COPY . /app 

# volume
EXPOSE 8000

# 本番はGunicornで起動
CMD ["gunicorn", "-w", "3", "-b", "0.0.0.0:8000", "config.wsgi:application"]

