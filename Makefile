run:
# 	docker compose start
	docker compose exec web python3 manage.py load_tasks
    docker compose exec web python3 manage.py migrate
	docker compose exec web python3 manage.py load_pasts
