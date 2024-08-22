FROM ubuntu:latest
LABEL authors="leonardo@lhes.tech"

WORKDIR /app

COPY . .

ENTRYPOINT ["top", "-b"]