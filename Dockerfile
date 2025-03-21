FROM python:3.12.8-slim


WORKDIR /app

COPY . /app

RUN pip install -r req.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]