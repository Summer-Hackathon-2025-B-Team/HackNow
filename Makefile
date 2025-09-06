# テーブルのマイグレーション＋各テーブルの一括登録
run:
	docker compose exec web python3 manage.py migrate
	docker compose exec web python3 manage.py load_pasts
	