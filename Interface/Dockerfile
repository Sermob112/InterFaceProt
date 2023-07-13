# Используем базовый образ Python
FROM python:3.11

# Установка переменной окружения PYTHONUNBUFFERED в 1 для отключения буферизации вывода
ENV PYTHONUNBUFFERED=1

# Установка рабочей директории в /app
WORKDIR /app

# Установка зависимостей проекта
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Копирование кода проекта в контейнер
COPY . /app/

# Запуск команды при запуске контейнера
CMD python manage.py runserver 0.0.0.0:8000