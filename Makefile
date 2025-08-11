run:
	docker compose exec web python3 manage.py migrate
	docker compose exec web python3 manage.py load_pasts
	docker compose exec web python manage.py createsuperuser
