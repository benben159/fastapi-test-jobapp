FROM python:3.9-slim-bookworm

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD [ "uvicorn", "main:app", "--host=0.0.0.0", "--port=1080" ]
