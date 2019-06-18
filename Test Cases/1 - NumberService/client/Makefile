#Docker stuff
build:
	docker build --rm --tag malloc1024/number-service-client:test .

start:
	docker run --network host --name client -it --rm malloc1024/number-service-client:test

push:
	docker push malloc1024/number-service-client:test

pull:
	docker pull malloc1024/number-service-client:test

clean:
	docker container prune -f; \
	docker image prune -f
