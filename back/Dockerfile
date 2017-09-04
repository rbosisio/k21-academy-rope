FROM python:3.5-alpine

COPY . /app
WORKDIR /app

RUN pip install -r requirement.txt

EXPOSE 8000

ENTRYPOINT ["gunicorn", "-w 3", "-b :8000", "back.wsgi"]
