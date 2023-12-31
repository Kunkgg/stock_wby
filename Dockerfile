FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt -i https://mirrors.aliyun.com/pypi/simple

COPY ./src /code/src

CMD ["python", "/code/src/main.py"]

