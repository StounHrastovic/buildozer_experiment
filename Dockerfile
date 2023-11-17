# Этап 1: Копирование основных файлов проекта и установка buildozer
FROM python:3.11.4-slim as builder

# Устанавливаем buildozer
RUN pip install python-for-android==0.7 && \
    pip install --upgrade pip && \
    pip install buildozer

# Устанавливаем переменную окружения, чтобы не создавать кэш pyc-файлов
ENV PYTHONDONTWRITEBYTECODE=1

# Устанавливаем рабочий каталог
WORKDIR /app

# Копируем buildozer.spec в контейнер
COPY buildozer.spec /app/buildozer.spec

# Копируем все остальные файлы проекта
COPY . /app

# Выводим информацию о версии buildozer при запуске контейнера
CMD ["buildozer", "version"]
