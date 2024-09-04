FROM python:3.7-slim

WORKDIR /app

COPY api/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY api/src /app/src
COPY datasample.csv /app/

ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000

CMD ["python", "src/main.py"]
