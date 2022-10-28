show-public-ip
===
A simple web server that outputs the container's public ip address as a web site.
There are two routes available:
- / shows an http site
- /api show only the api

# Supported tags and respective Dockerfile links

* [`latest` (latest/Dockerfile)](https://github.com/Martinay/show-public-ip/blob/master/Dockerfile)

For more information about this image and its history, please have a look at [`martinay/show-public-ip` GitHub repo](https://github.com/Martinay/show-public-ip).

# What is show-public-ip?
[show-public-ip](https://github.com/Martinay/show-public-ip) is a simple web site to show the container's public IP address, written in javascript.

# How to use this image?
The docker image is auto built at [https://registry.hub.docker.com/u/martinay/show-public-ip/](https://registry.hub.docker.com/u/martinay/show-public-ip/).

## Local Run
```sh
$ docker run --rm -it -p 80:80 martinay/show-public-ip
```

with custom port:
```sh
$ docker run --rm -it -e PORT=1234 -p 1234:1234 martinay/show-public-ip
```

# Which image is based on?
The image is based on node:lts-alpine
