FROM nginx:latest
RUN mkdir -p /data/nginx/cache
COPY confd.conf /etc/nginx/conf.d/confd.conf
COPY nginx.conf /etc/nginx/nginx.conf
