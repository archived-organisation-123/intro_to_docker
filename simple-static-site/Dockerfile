FROM nginx
COPY entrypoint.sh /
RUN chmod +x entrypoint.sh
COPY html /usr/share/nginx/html
CMD [ "./entrypoint.sh" ]