FROM python:3.8.6-alpine
WORKDIR /license_plate
ADD . /license_plate
RUN apk update
RUN apk add gcc
RUN apk add libc-dev
RUN pip install -r requirements.txt
CMD ["python", "app.py"]