FROM python:3.11-slim

WORKDIR /app

# Install dependencies in one layer, clean up after
RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files (least frequently changed first)
COPY launch.sh help.txt ./
COPY code/ code/

RUN chmod +x launch.sh

CMD ["./launch.sh"]