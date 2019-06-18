FROM alpine:3.9

WORKDIR /docker

RUN apk add --no-cache python3
RUN pip3 --no-cache-dir install pipenv==2018.11.26

#Pipenv is stupid.
#See the Dockerfile for server.py for an explanation of why.
RUN pipenv install --python 3.6
COPY Pipfile.lock /docker/Pipfile.lock
RUN pipenv sync
RUN rm Pipfile Pipfile.lock

#Copy over the client script
COPY client.py /docker/client.py

ENTRYPOINT ["pipenv", "run", "python", "client.py"]
CMD ["127.0.0.1:80"]
