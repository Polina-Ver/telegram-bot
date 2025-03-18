FROM python:3.12-slim

WORKDIR /telegram-bot

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD ["python3", "-u", "main.py"]
