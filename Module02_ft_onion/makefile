all:
	docker compose up -d

log:
	docker compose up

ps:
	docker compose ps

stop:
	docker compose stop

down:
	docker compose down -v

clean: down
	docker system prune -f -a --volumes

re: clean all