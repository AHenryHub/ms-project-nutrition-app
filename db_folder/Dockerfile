FROM python:slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5001

CMD ["python", "main.py"]

COPY requirements.txt requirements.txt