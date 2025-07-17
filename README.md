# HackNow
Collaborative task management for hackathon teams.

### 開発環境
- Python 3.10
- Django 5.2
- MySQL 8.0
- Docker / Docker Compose

### ディレクトリ構造（開発前段階）
```
HackNow/  
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
|--- .env.sample #環境変数のテンプレート  
|--- docker-compose.yml  
|--- requirements.txt  
|___ README.md
```
### 環境変数の設定

まず`.env`ファイルを作成します:
```
#bash
cp .env.sample .env
```

**🔑SECRET_KEY生成方法**
```
#bash
python -c "import secrets; print(secrets.token_urlsafe(50))"
```

**.envの中身は以下のように設定してください(サンプル):**
```
# ======= ✅ チームで共通にする設定 =======
MYSQL_DATABASE=django_db             　　　# 開発環境で使うデータベース名（チームで共通・固定）
MYSQL_USER=dev_user                  　　　# 開発用のデータベースユーザ名（チーム共通）
DJANGO_TIME_ZONE=Asia/Tokyo          　　　# タイムゾーン設定(全員共通)
DJANGO_LANGUAGE_CODE=ja              　　　# 言語コード設定(全員共通)
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1  # 許可するホスト。必要に応じて各自で追加可能

# ======= 🔧 各自で変更する設定 =======
MYSQL_PASSWORD=your_own_password     # 各自がローカル環境で設定するDBユーザーパスワード(環境開発で各自設定、非公開)
MYSQL_ROOT_PASSWORD=your_root_pw     # MYSQLのrootパスワード(開発環境で各自設定、非公開)
DJANGO_SECRET_KEY=your_secret_key    # Djangoのセキュリティキー(必ず各自で生成すること)
DJANGO_DEBUG=True                    # デバッグモード設定。開発中はTrue、本番や検証環境はFalse推奨


```

### 開発環境立ち上げ
```
#bash
docker compose up --build
```


### 初回セットアップ
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

