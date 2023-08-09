FROM python:3.10
# устанавливаем рабочую директорию
WORKDIR /home/app
# устанавливаем переменную окружения для проекта
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get autoremove && \
    apt-get autoclean && \
    apt-get install -y vim


RUN pip install --upgrade pip

# Копирование файлов проекта в образ

COPY ./requirements.txt /home/app/requirements.txt
# устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

COPY . /home/app
RUN chmod +x /home/app/entrypoint.sh && chmod -R 755 /home/app
ENTRYPOINT ["/home/app/entrypoint.sh"]
