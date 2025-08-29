# config/settings.py  （本番用）

import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(dotenv_path=BASE_DIR / '.env.prod')

# --- 基本 ---
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "!!!-replace-me-in-production-!!!")
DEBUG = os.getenv("DJANGO_DEBUG", "false").lower() == "true"

# カンマ区切りを配列へ
def _csv(name: str, default: str = ""):
    return [x.strip() for x in os.getenv(name, default).split(",") if x.strip()]

ALLOWED_HOSTS = _csv("DJANGO_ALLOWED_HOSTS", "")
CSRF_TRUSTED_ORIGINS = _csv("DJANGO_CSRF_TRUSTED_ORIGINS", "")

# CSRF_TRUSTED_ORIGINS が未指定なら、ALLOWED_HOSTS から https:// を推定
if not CSRF_TRUSTED_ORIGINS and ALLOWED_HOSTS:
    CSRF_TRUSTED_ORIGINS = [f"https://{h}" for h in ALLOWED_HOSTS if h not in ("localhost", "127.0.0.1")]

# ALB/リバプロ越しの HTTPS 終端
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# --- アプリ ---
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "apps.user.apps.UserConfig",
    "apps.home.apps.HomeConfig",
    "apps.task.apps.TaskConfig",
    "apps.course.apps.CourseConfig",
    "apps.team.apps.TeamConfig",
    "apps.knowledge.apps.KnowledgeConfig",
    "apps.past.apps.PastConfig",
    "apps.meeting.apps.MeetingConfig",
    "apps.document.apps.DocumentConfig",
    "apps.reference.apps.ReferenceConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "config.middleware.authMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [{
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "DIRS": [BASE_DIR / "templates"],
    "APP_DIRS": True,
    "OPTIONS": {"context_processors": [
        "django.template.context_processors.debug",
        "django.template.context_processors.request",
        "django.contrib.auth.context_processors.auth",
        "django.contrib.messages.context_processors.messages",
    ]},
}]

WSGI_APPLICATION = "config.wsgi.application"

# --- DB（本番=RDS / 開発=docker-compose の db） ---
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.getenv("MYSQL_DB") or os.getenv("MYSQL_DATABASE"),
        "USER": os.getenv("MYSQL_USER"),
        "PASSWORD": os.getenv("MYSQL_PASSWORD"),
        "HOST": os.getenv("MYSQL_HOST", "db"),
        "PORT": os.getenv("MYSQL_PORT", "3306"),
        "OPTIONS": {
            "charset": "utf8mb4",
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}
# コネクション再利用（秒）
CONN_MAX_AGE = int(os.getenv("DJANGO_CONN_MAX_AGE", "60"))

# --- I18N ---
LANGUAGE_CODE = os.getenv("DJANGO_LANGUAGE_CODE", "ja")
TIME_ZONE = os.getenv("DJANGO_TIME_ZONE", "Asia/Tokyo")
USE_I18N = True
USE_TZ = True

# --- Static ---
STATIC_URL = "/static/"
# 本番は collectstatic でここに集約（docker-compose で /app/staticfiles を volume マウント）
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATICFILES_DIRS = [
        BASE_DIR / "static"
]

# --- セキュリティ（本番系） ---
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG
X_FRAME_OPTIONS = "DENY"
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_REFERRER_POLICY = "same-origin"
# HSTS は最初は無効にしておき、安定後に有効化推奨
# SECURE_HSTS_SECONDS = 31536000
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True

# --- その他 ---
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_USER_MODEL = "user.User"
LOGIN_URL = "user:login"
<<<<<<< HEAD

# ログイン後の遷移先（オープニング画面）
LOGIN_REDIRECT_URL = "home:opening"

# ログアウト時の遷移先（ログイン画面）
=======
LOGIN_REDIRECT_URL = "home:index"
>>>>>>> a62204d (Keep local settings change)
LOGOUT_REDIRECT_URL = "user:login"

# --- ロギング（Gunicorn/コンテナ標準出力へ） ---
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "root": {"handlers": ["console"], "level": "INFO"},
}

