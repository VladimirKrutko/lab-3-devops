FROM python:3.10

RUN apt-get update && apt-get install -y \
    git \
 && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/VladimirKrutko/lab-3-devops.git /app
WORKDIR /app

RUN pip install -r requirements.txt

RUN python manage.py makemigrations
RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
