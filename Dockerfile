
FROM python:3.9.1

# Подтянуть зависимости проекта через докер
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Монтируем образ
COPY . tkursach
WORKDIR /tkursach

# Делаем джанговские миграции
RUN python ./manage.py migrate

# Собираем статические файлы
RUN python ./manage.py collectstatic

# Пробрасываем 8000-й порт в докер
EXPOSE 8000

# Запускаем отладочный веб-сервер
ENTRYPOINT ["python", "./manage.py"]
CMD ["runserver", "127.0.0.1:8000"]