FROM python:3.6.4-alpine
LABEL Description="runs a website to show the container's public Ip"
LABEL maintainer="martinay1"
EXPOSE 80
WORKDIR /code
COPY index.py /code
RUN pip install requests
ENTRYPOINT python index.py