#Docker stuff
build:
	docker build --rm --tag malloc1024/number-service-server:test .

start:
	docker run -d --name server -p 80:80 --rm malloc1024/number-service-server:test

stop:
	docker container stop server

push:
	docker push malloc1024/number-service-server:test

pull:
	docker pull malloc1024/number-service-server:test

clean:
	docker container prune -f; \
	docker image prune -f
