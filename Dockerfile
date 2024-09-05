FROM python:3.11.6

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8005

ENV NAME WordCount

CMD ["uvicorn", "main.py:app", "--host", "0.0.0.0", "--port", "8005"]