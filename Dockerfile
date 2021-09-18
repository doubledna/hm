FROM docker.io/python:3.8.9-alpine3.13

RUN mkdir -p /app
WORKDIR /app

ADD hmc.tgz ./
RUN tar -zxvf hmc.tgz \
    && rm -rf hmc.tgz \
    && pip install -i https://mirrors.aliyun.com/pypi/simple --quiet --trusted-host=mirrors.aliyun.com -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:38080"]
