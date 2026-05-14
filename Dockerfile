FROM python:3.11.9-slim

WORKDIR / app

COPY . .

RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    && rm -rf /var/lin/apt/lists/*

RUN pip install --no-cache-dir \
    pandas==2.2.3 \
    numpy==2.1.3 \
    scikit-learn==1.5.2 \
    matplotlib==3.9.2

CMD ["python", "main.py"]
