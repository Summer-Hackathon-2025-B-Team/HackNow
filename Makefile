# テーブルのマイグレーション＋各テーブルの一括登録
run:
	docker compose exec web python3 manage.py migrate
	docker compose exec web python3 manage.py load_pasts
	docker compose exec web python3 manage.py load_references
	docker compose exec web python3 manage.py load_courses
	docker compose exec web python3 manage.py load_teams
	docker compose exec web python3 manage.py load_users
	