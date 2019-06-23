FROM alpine:latest

RUN apk update && apk upgrade && apk add nginx &&  rm -rf /var/cache/apk/* && mkdir -p /run/nginx

COPY default.conf /etc/nginx/conf.d/default.conf
COPY index.html /usr/share/nginx/html/

VOLUME ["/var/cache/nginx"]

EXPOSE 80

CMD /usr/sbin/nginx -g "daemon off;"
