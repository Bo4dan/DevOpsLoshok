# nginx/Dockerfile
FROM nginx:stable-alpine

# Удалим конфигурацию по умолчанию и скопируем нашу
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/nginx.conf
