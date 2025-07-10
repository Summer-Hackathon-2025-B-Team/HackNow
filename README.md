# hacknest-teamb
Collaborative task management for hackathon teams.

<!-- 開発環境 -->
- Python 3.10
- Django 4.2
- MySQL 8.0
- Docker / Docker Compose

<!-- ディレクトリ構造（初期） -->

|--- app/ 
|--- docker/
|--- .env.example #環境変数のテンプレート
|--- docker-compose.yml
|___ README.md

<!-- 環境変数の設定 -->

まず`.env`ファイルを作成します:

```bash
cp .env.example.env

`.env`の中身は以下のように設定してください:
    MYSQL_DATABASE=django_db
    MYSQL_USER=django_user
    MYSQL_PASSWORD=devpassword
    MYSQL_ROOT_PASSWORD=rootpass
    DJANGO_SECRET_KEY=your_secret_key

<!-- 開発環境立ち上げ -->
```bash
docker compose up --build


