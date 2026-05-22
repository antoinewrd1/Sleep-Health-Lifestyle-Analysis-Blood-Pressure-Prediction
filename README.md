# Sleep Health \& Lifestyle Blood Pressure Prediction Platform

# Overview

# 

# This repository is a modular machine learning engineering platform for predicting systolic blood pressure using sleep health and lifestyle data. The project evolved from a single exploratory Jupyter notebook into a production-style application with:

# 

# reusable ML pipelines

# FastAPI prediction services

# Streamlit dashboard

# batch prediction workflows

# SQLite prediction logging

# monitoring and drift detection

# experiment tracking

# automated testing

# Docker support

# CI/CD workflows

# modular architecture

# 

# The project demonstrates real-world machine learning engineering practices including:

# 

# data validation

# preprocessing pipelines

# model comparison

# hyperparameter tuning

# prediction APIs

# monitoring utilities

# artifact persistence

# reporting

# testing

# automation

# Core Features

# Machine Learning Pipeline

# End-to-end regression workflow

# Config-driven training pipeline

# Feature engineering utilities

# Cross-validation

# Hyperparameter tuning

# Multiple model comparison

# Experiment tracking

# Models Included

# 

# The project compares:

# 

# Baseline Regressor

# Random Forest Regressor

# Gradient Boosting Regressor

# Support Vector Regressor (SVR)

# FastAPI Prediction Service

# 

# The repository includes a production-style API for prediction serving.

# 

# Features

# REST prediction endpoint

# request validation

# JSON responses

# prediction logging

# interactive API documentation

# Run API

# uvicorn src.api.main:app --reload

# Swagger Documentation

# http://127.0.0.1:8000/docs

# Streamlit Dashboard

# 

# Interactive dashboard for prediction visualization and inference.

# 

# Features

# interactive sliders

# prediction visualization

# real-time inference

# tabular summaries

# Run Dashboard

# streamlit run src/dashboard/app.py

# Batch Prediction Workflow

# 

# Supports running predictions against entire CSV datasets.

# 

# Features

# CSV batch inference

# output prediction files

# reusable prediction workflows

# 

# Main utility:

# 

# src/batch\_predict.py

# SQLite Prediction Logging

# 

# Prediction requests are automatically stored in SQLite.

# 

# Stored Information

# prediction timestamp

# model name

# input payload

# prediction result

# 

# Database utilities:

# 

# src/database/db.py

# Repository Structure

# Sleep-Health-Lifestyle-Analysis-Blood-Pressure-Prediction/

# │

# ├── .github/

# │   └── workflows/

# │       └── tests.yml

# │

# ├── config/

# │   └── model\_config.json

# │

# ├── data/

# │   └── Sleep\_Health\_and\_Lifestyle\_Dataset.csv

# │

# ├── docs/

# │   ├── architecture.md

# │   ├── artifact\_strategy.md

# │   ├── data\_dictionary.md

# │   ├── deployment\_notes.md

# │   ├── model\_card.md

# │   ├── modeling\_decisions.md

# │   ├── monitoring\_plan.md

# │   ├── quality\_checklist.md

# │   └── testing\_strategy.md

# │

# ├── models/

# │

# ├── notebooks/

# │

# ├── outputs/

# │

# ├── reports/

# │

# ├── scripts/

# │   ├── full\_pipeline.ps1

# │   ├── health\_check.ps1

# │   ├── run\_all.ps1

# │   └── run\_project.ps1

# │

# ├── src/

# │   ├── api/

# │   │   ├── \_\_init\_\_.py

# │   │   └── main.py

# │   │

# │   ├── dashboard/

# │   │   └── app.py

# │   │

# │   ├── database/

# │   │   ├── \_\_init\_\_.py

# │   │   └── db.py

# │   │

# │   ├── \_\_init\_\_.py

# │   ├── batch\_predict.py

# │   ├── config\_loader.py

# │   ├── data\_loader.py

# │   ├── data\_profile.py

# │   ├── evaluation.py

# │   ├── experiment\_tracker.py

# │   ├── feature\_engineering.py

# │   ├── health\_check.py

# │   ├── logger.py

# │   ├── model\_metadata.py

# │   ├── model\_registry.py

# │   ├── monitoring.py

# │   ├── persistence.py

# │   ├── pipelines.py

# │   ├── predict.py

# │   ├── reporting.py

# │   ├── results\_manager.py

# │   ├── schema.py

# │   └── validation.py

# │

# ├── tests/

# │   ├── test\_api.py

# │   ├── test\_batch\_predict.py

# │   ├── test\_config\_loader.py

# │   ├── test\_data\_profile.py

# │   ├── test\_database.py

# │   ├── test\_evaluation.py

# │   ├── test\_experiment\_tracker.py

# │   ├── test\_feature\_engineering.py

# │   ├── test\_health\_check.py

# │   ├── test\_model\_registry.py

# │   ├── test\_monitoring.py

# │   ├── test\_persistence.py

# │   ├── test\_pipelines.py

# │   ├── test\_predict.py

# │   ├── test\_reporting.py

# │   ├── test\_results\_manager.py

# │   ├── test\_schema.py

# │   └── test\_validation.py

# │

# ├── .dockerignore

# ├── .gitignore

# ├── CHANGELOG.md

# ├── CONTRIBUTING.md

# ├── Dockerfile

# ├── pytest.ini

# ├── README.md

# ├── requirements.txt

# └── train.py

# Data Processing Workflow

# 1\. Data Loading

# 

# The dataset is loaded from:

# 

# data/Sleep\_Health\_and\_Lifestyle\_Dataset.csv

# 2\. Data Validation

# 

# Validation checks include:

# 

# required columns

# schema validation

# numeric range checks

# blood pressure formatting

# duplicate row detection

# feature drift monitoring

# 3\. Feature Engineering

# 

# Transformations include:

# 

# splitting Blood Pressure into:

# Systolic

# Diastolic

# missing value handling

# categorical encoding

# numeric scaling

# 4\. Pipeline Construction

# Numeric Pipeline

# median imputation

# standard scaling

# Categorical Pipeline

# most frequent imputation

# one-hot encoding

# 5\. Model Training

# 

# The pipeline supports:

# 

# baseline comparison

# model registries

# reusable parameter grids

# cross-validation

# hyperparameter tuning

# 6\. Monitoring \& Drift Detection

# 

# Monitoring utilities support:

# 

# schema comparison

# feature drift detection

# prediction distribution summaries

# Running the Project

# Create Virtual Environment

# python -m venv .venv

# Activate Environment (Windows)

# .\\.venv\\Scripts\\Activate.ps1

# Install Dependencies

# pip install -r requirements.txt

# Run ML Pipeline

# python train.py

# Run API

# uvicorn src.api.main:app --reload

# Run Dashboard

# streamlit run src/dashboard/app.py

# Run Tests

# python -m pytest

# Run PowerShell Health Checks

# .\\scripts\\health\_check.ps1

# Docker Support

# Build Image

# docker build -t sleep-health-platform .

# Run Container

# docker run sleep-health-platform

# Continuous Integration

# 

# GitHub Actions automatically runs:

# 

# pytest suite

# repository validation

# 

# Workflow:

# 

# .github/workflows/tests.yml

# Outputs \& Artifacts

# 

# Generated artifacts may include:

# 

# outputs/

# reports/

# models/

# 

# Example artifacts:

# 

# predictions.csv

# test\_results.csv

# cross\_validation\_results.csv

# model\_report.md

# experiment\_metadata.json

# monitoring\_summary.json

# trained model artifacts

# Testing Strategy

# 

# The repository includes automated tests for:

# 

# API endpoints

# batch prediction

# monitoring utilities

# persistence

# reporting

# pipelines

# feature engineering

# validation

# experiment tracking

# database logging

# Monitoring Strategy

# 

# Monitoring utilities support:

# 

# schema drift

# feature drift

# prediction summaries

# monitoring metadata

# 

# Documentation:

# 

# docs/monitoring\_plan.md

# Experiment Tracking

# 

# Experiment metadata includes:

# 

# model name

# metrics

# timestamps

# dataset statistics

# training row counts

# Documentation

# 

# Additional documentation is available in:

# 

# docs/

# 

# Including:

# 

# architecture

# testing strategy

# deployment notes

# artifact strategy

# model card

# data dictionary

# monitoring plan

# Reproducibility

# 

# This project emphasizes reproducibility through:

# 

# pinned dependency versions

# Docker support

# config-driven execution

# automated testing

# CI workflows

# relative file paths

# experiment tracking

# Future Improvements

# 

# Potential future enhancements include:

# 

# MLflow integration

# SHAP explainability

# cloud deployment

# Airflow orchestration

# Databricks integration

# feature store support

# model registry versioning

# scheduled retraining

# streaming inference

# Disclaimer

# 

# This repository is intended for educational and machine learning engineering demonstration purposes only.

# 

# The models included are not intended for clinical diagnosis or medical decision-making.

