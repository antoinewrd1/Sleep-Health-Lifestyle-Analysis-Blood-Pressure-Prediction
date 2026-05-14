FROM python:3.11.9-slim

WORKDIR / app

COPY . .

RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir \
    pandas==2.2.3 \
    numpy==2.1.3 \
    scikit-learn==1.5.2 \
    matplotlib==3.9.2 \
    seaborn==0.13.2 \
    notebook==7.2.2 \
    jupyter==1.1.1

CMD ["jupyter", "nbconvert", "--to", "notebook", "--execute", "Sleep_health_and_lifestyle_dataset.ipynb", "--output", "Repo_1.ipynb"]
