FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get update \
    && apt-get install -y ffmpeg \
    && python3 -m venv .venv \
    && . .venv/bin/activate \
    && pip install --no-cache-dir -U pip \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY launch.sh .
COPY env/ env/
COPY code/ code/
COPY help.txt .

RUN chmod +x launch.sh

CMD ["./launch.sh"]