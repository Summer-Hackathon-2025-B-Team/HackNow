# hacknest-teamb
Collaborative task management for hackathon teams.

### 開発環境
- Python 3.10
- Django 4.2
- MySQL 8.0
- Docker / Docker Compose

### ディレクトリ構造（開発前段階）
```
hacknest-teamb/  
|--- app/
|    |--- apps/
|    |--- config
|    |    |--- asgi.py
|    |    |--- settings.py
|    |    |--- urls.py
|    |    |--- wsgi.py
|    |--- manage.py
|    |--- templates/
|    |--- static/
|    |    |--- css/
|    |    |--- js/
|    |    |--- images/
|    |--- sql/
|--- docker/  
|    |--- Dockerfile
|--- .env  
|--- .env.example #環境変数のテンプレート  
|--- docker-compose.yml  
|--- requirements.txt  
|___ README.md
```
### 環境変数の設定

まず`.env`ファイルを作成します:

```
#bash
cp .env.example.env
```

**.envの中身は以下のように設定してください(サンプル):**
```
# ======= ✅ チームで共通にする設定 =======
MYSQL_DATABASE=dev_db                 # 開発用のDB名（固定でよい）
MYSQL_USER=dev_user                   # 開発用のDBユーザー（共通でよい）
DJANGO_TIME_ZONE=Asia/Tokyo          # 全員同じ
DJANGO_LANGUAGE_CODE=ja              # 全員同じ
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1  # 必要があれば各自追加

# ======= 🔧 各自で変更する設定 =======
MYSQL_PASSWORD=your_own_password     # 各自のローカルで設定したいパスワード
MYSQL_ROOT_PASSWORD=your_root_pw     # 通常は開発用に各自で設定（Gitに含めない）

DJANGO_SECRET_KEY=your_secret_key    # セキュリティ上必ず各自で生成する
DJANGO_DEBUG=True                    # デバッグするならTrue、本番や検証ではFalse

```

###  🔑SECRET_KEY生成方法
```
#bash
python -c "import secrets; print(secrets.token_urlsafe(50))"
```

### 開発環境立ち上げ
```
#bash
docker compose up --build
```

### 初回セットアップ(まだやらない)
1.データベースマイグレーション：
```
#bash
docker compose exec web python manage.py migrate
```
2.管理者ユーザー作成：
```
#bash
docker compose exec web python manage.py createsuperuser
```

### アクセス方法
Webアプリ： http://localhost:8000

