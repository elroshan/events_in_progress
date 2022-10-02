FROM python:3.9-slim-buster
WORKDIR /app

COPY . /app
WORKDIR /app/src

ENTRYPOINT ["/bin/bash"]
