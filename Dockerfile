FROM hm:v1
WORKDIR /hm
COPY requirements.txt .
RUN /usr/local/bin/python -m pip install -i https://mirrors.aliyun.com/pypi/simple --upgrade pip
RUN pip install -i https://mirrors.aliyun.com/pypi/simple --trusted-host=mirrors.aliyun.com --no-cache-dir -r requirements.txt
COPY . .
RUN python manage.py migrate
CMD ["python", "manage.py", "runserver", "0.0.0.0:38080"]