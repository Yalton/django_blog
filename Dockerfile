#Blog (Dockerfile)
FROM python:3

WORKDIR /opt/django_Blog/django_root:/usr/src/app

RUN pip install Django google-api-core google-auth google-cloud-core google-cloud-storage google-crc32c google-resumable-media googleapis-common-protos Pillow pylint pylint-django pylint-plugin-utils channels channels_redis django-redis redis-simple-cache mysqlclient django-mptt django-embed-video

CMD [ "python", "./manage.py",  "runserver",  "0.0.0.0:8000"]
