FROM python:3.8

WORKDIR /home

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p sre-intern-test

USER root

COPY . .

ENTRYPOINT ["bash"]# docker run --name apliccation app_python