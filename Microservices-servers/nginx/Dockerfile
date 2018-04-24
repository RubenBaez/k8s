FROM tutum/nginx
RUN rm /etc/nginx/sites-enabled/default
ADD sites-enabled/ /etc/nginx/sites-enabled

ADD static/ /www/static

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

