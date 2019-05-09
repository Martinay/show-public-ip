show-public-ip
===
A simple web server that outputs the container's public ip address.

route / shows an http site
route /api show only the api

# Supported tags and respective Dockerfile links

* [`latest` (latest/Dockerfile)](https://github.com/Martinay/show-public-ip/blob/master/Dockerfile)

For more information about this image and its history, please see the relevant manifest file in the [`martinay/show-public-ip` GitHub repo](https://github.com/Martinay/show-public-ip).

# What is show-public-ip?
[show-public-ip](https://github.com/Martinay/show-public-ip) is a simple web site to show the container's public IP address, written in python.

# How to use this image?
The docker image is auto built at [https://registry.hub.docker.com/u/martinay1/show-public-ip/](https://registry.hub.docker.com/u/martinay1/show-public-ip/).

## Local Run
```sh
$ docker run --rm -it -p 80:80 martinay1/show-public-ip
```

# Which image is based on?
The image is based on python:3.6.4-alpine

# What has been changed?
Added the index.py code.