FROM alpine:3.9

WORKDIR /docker

RUN apk add --no-cache python3
RUN pip3 --no-cache-dir install pipenv==2018.11.26

#Pipenv is stupid.
#Essentially, 'pipenv install' uses the Pipfile if it exists,
#or creates one and overwrites the Pipfile.lock with an empty
#one.On the other hand, 'pipenv sync' uses the Pipfile.lock,
#but it fails if there's no Pipfile present.
#'pipenv install --deploy --ignore-pipfile' should work,
#but after playing around with it, it seems brittle...
#The solution: Create an empty Pipfile, copy the correct
#Pipfile.lock over, and then use it to install the dependencies.
RUN pipenv install --python 3.6
COPY Pipfile.lock /docker/Pipfile.lock
RUN pipenv sync
RUN rm Pipfile Pipfile.lock

#Copy over the server script
COPY server.py /docker/server.py

#Documents that our server will be running on port 80 within the container.
#This does not actually publish the port, it's only documentation.
EXPOSE 80

ENTRYPOINT ["pipenv", "run", "gunicorn", "server:app"]
CMD ["--workers=4", "--bind=0.0.0.0:80"]
