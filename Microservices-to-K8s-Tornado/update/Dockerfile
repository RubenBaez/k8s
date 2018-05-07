FROM python:3.4-jessie

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

#ENTRYPOINT ["gunicorn"]
ENTRYPOINT ["python"]
#CMD ["-w", "2", "-b", ":8000", "app:app"]
CMD ["app.py"]

