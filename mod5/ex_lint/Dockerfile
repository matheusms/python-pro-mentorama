# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 intall -r requirements.txt

COPY . .

CMD [ "python3", "exemplo_lint.py"]