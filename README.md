# hacknest-teamb
Collaborative task management for hackathon teams.

### 開発環境
- Python 3.10
- Django 4.2
- MySQL 8.0
- Docker / Docker Compose

### ディレクトリ構造（初期）
```
hacknest-teamb/  
| app/  
|    |--- manage.py/  
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

**.envの中身は以下のように設定してください:**
```
MYSQL_DATABASE=django_db
MYSQL_USER=django_user
MYSQL_PASSWORD=devpassword
MYSQL_ROOT_PASSWORD=rootpass
DJANGO_SECRET_KEY=your_secret_key
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

