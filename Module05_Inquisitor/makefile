all:
	docker compose up -d

server:
	docker exec -it server /bin/bash

client:
	docker exec -it client /bin/bash

inquisitor:
	docker exec -it inquisitor /bin/bash

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