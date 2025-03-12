FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cashe-dit -r requirements.txt

COPY . .
CMD ["python3", "-u", "main.py"]
