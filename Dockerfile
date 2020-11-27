FROM python:3.8-alpine3.11

RUN apk add -U chromium chromium-chromedriver

ARG project_dir=/python/app/
ADD . ${project_dir}
WORKDIR ${project_dir}

RUN set -x && \
    pip3 install --upgrade pip && \
    pip3 install -r requirements.txt

CMD ["python3", "main.py"]