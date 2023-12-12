NAME	:= stockholm

all:
	docker build -t ${NAME} .

bash:
	docker run -it --name ${NAME} ${NAME} 

stop:
	docker stop ${NAME}

rm:
	docker rm ${NAME}
	docker image rm ${NAME}

clean: rm
	docker system prune -f -a --volumes

re: clean all