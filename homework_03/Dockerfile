FROM python:3.11.7-bookworm

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY app.py ./

CMD ["uvicorn", "app:app", "--host=0.0.0.0", "--port=8000"]

EXPOSE 8000

# docker build . -t web - команда для сборки образа, выполнять из директории homework_03
# docker run -it -P web - команда для запуска контейнера с приложением
# для просмотра порта локального хоста использовать docker ps