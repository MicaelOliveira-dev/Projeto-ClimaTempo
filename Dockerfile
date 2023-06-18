FROM python:3.8

WORKDIR  /code
COPY requeriments.txt .

RUN apt-get update 
RUN pip install -r requeriments.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


