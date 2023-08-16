FROM python:3.8
WORKDIR /app
COPY . /app
RUN apt-get update && apt-get install -y sqlite3 libsqlite3-dev
RUN pip install -r requirements.txt
CMD ["python", "myscraper.py"]

