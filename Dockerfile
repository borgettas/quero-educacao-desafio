FROM python:3.8

RUN useradd --create-home --shell /bin/bash app_user

WORKDIR /home

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

USER app_user

COPY . .

ENTRYPOINT ["bash"]# docker run --name apliccation app_python