ARG IMAGE_TAG=8.3.26
FROM ultralytics/ultralytics:$IMAGE_TAG
WORKDIR /app

COPY app /app/
RUN pip3 install --upgrade pip && pip install --no-cache-dir Flask uwsgi && \
  wget -P weights/ https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo11n.pt
EXPOSE 80
CMD ["uwsgi", "--http", "0.0.0.0:80", "--master", "-p", "4", "-w", "app:app"]
