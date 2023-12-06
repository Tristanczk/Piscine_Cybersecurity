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
	ssh-keygen -f "/mnt/nfs/homes/tczarnia/.ssh/known_hosts" -R "[localhost]:8086"

re: clean all