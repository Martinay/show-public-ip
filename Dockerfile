FROM node:lts-alpine
LABEL Description="runs a website to show the container's public Ip"
LABEL maintainer="martinay"
EXPOSE 80
WORKDIR /code
COPY /server /code
RUN npm install
ENTRYPOINT node server.js