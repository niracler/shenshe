FROM python:3.6

USER root
ENV PYTHONUNBUFFERED=0
ENV PYTHONIOENCODING=utf-8

RUN python3 -m pip install redis

COPY spider.py spider.py
CMD python3 spider.py