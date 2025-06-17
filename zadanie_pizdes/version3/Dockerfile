# version1/Dockerfile (аналогично для version2 и version3)
FROM python:3.9-slim

# Перейдём в рабочую директорию
WORKDIR /app

# Установим переменные окружения для режима разработки Flask
ENV FLASK_ENV=development
ENV FLASK_APP=app.py

# Скопируем зависимости и установим Flask
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Скопируем код приложения
COPY . .

# Запустим встроенный веб-сервер Flask на 0.0.0.0
CMD ["flask", "run", "--host=0.0.0.0"]
