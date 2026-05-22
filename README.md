# Sleep Health \& Lifestyle Blood Pressure Prediction

# Overview

# 

# This project is a modular machine learning pipeline for predicting systolic blood pressure using sleep health and lifestyle data. The repository was refactored from an exploratory Jupyter notebook into a production-style Python project with reusable modules, automated testing, configuration management, reporting utilities, monitoring tools, Docker support, and CI workflows.

# 

# The project demonstrates end-to-end machine learning engineering practices including:

# 

# data loading

# schema validation

# feature engineering

# preprocessing pipelines

# model training

# hyperparameter tuning

# evaluation

# reporting

# experiment tracking

# monitoring

# persistence

# automated testing

# Project Objectives

# 

# The primary objective of this project is to analyze relationships between lifestyle variables and blood pressure while demonstrating a scalable machine learning workflow.

# 

# The project predicts:

# 

# Systolic Blood Pressure

# 

# using features such as:

# 

# sleep duration

# quality of sleep

# stress level

# physical activity

# heart rate

# BMI category

# daily steps

# occupation

# sleep disorder classification

# Models Included

# 

# The project compares multiple regression models:

# 

# Baseline Regressor

# Random Forest Regressor

# Gradient Boosting Regressor

# Support Vector Regressor (SVR)

# Evaluation Metrics

# 

# Models are evaluated using:

# 

# Mean Absolute Error (MAE)

# Mean Squared Error (MSE)

# Root Mean Squared Error (RMSE)

# R² Score

# 

# RMSE is used as the primary comparison metric.

# 

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

# │   ├── \_\_init\_\_.py

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

# │   ├── test\_config\_loader.py

# │   ├── test\_data\_profile.py

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

# 

# using reusable utilities in:

# 

# src/data\_loader.py

# 2\. Data Validation

# 

# Validation checks include:

# 

# required columns

# missing values

# duplicate rows

# blood pressure formatting

# numeric range validation

# schema consistency

# 

# Validation logic is stored in:

# 

# src/validation.py

# src/schema.py

# 3\. Feature Engineering

# 

# The pipeline performs transformations including:

# 

# splitting Blood Pressure into:

# Systolic

# Diastolic

# filling missing Sleep Disorder values

# preprocessing categorical variables

# scaling numeric features

# 

# Feature engineering logic is located in:

# 

# src/feature\_engineering.py

# 4\. Pipeline Construction

# 

# Preprocessing pipelines include:

# 

# Numeric Pipeline

# median imputation

# standard scaling

# Categorical Pipeline

# most frequent imputation

# one-hot encoding

# 

# Pipeline utilities are stored in:

# 

# src/pipelines.py

# 5\. Model Training

# 

# The project trains multiple candidate models using reusable model registries and parameter grids.

# 

# Training utilities include:

# 

# src/model\_registry.py

# src/evaluation.py

# 6\. Monitoring \& Drift Detection

# 

# Monitoring utilities support:

# 

# schema comparison

# numeric drift detection

# prediction distribution summaries

# 

# Monitoring utilities are located in:

# 

# src/monitoring.py

# Configuration Management

# 

# Configuration is handled through:

# 

# config/model\_config.json

# 

# Example configuration:

# 

# {

# &#x20; "target\_column": "Systolic",

# &#x20; "drop\_columns": \[

# &#x20;   "Systolic",

# &#x20;   "Diastolic"

# &#x20; ],

# &#x20; "test\_size": 0.2,

# &#x20; "random\_state": 42,

# &#x20; "cv\_folds": 5,

# &#x20; "models": \[

# &#x20;   "Baseline",

# &#x20;   "Random Forest",

# &#x20;   "Gradient Boosting",

# &#x20;   "SVR"

# &#x20; ]

# }

# Running the Project

# Create Virtual Environment

# python -m venv .venv

# Activate Environment (Windows)

# .\\.venv\\Scripts\\Activate.ps1

# Install Dependencies

# pip install -r requirements.txt

# Run Training Pipeline

# python train.py

# Running Tests

# 

# The project uses pytest for automated testing.

# 

# Run Test Suite

# python -m pytest

# PowerShell Automation Scripts

# 

# The repository includes automation scripts for project validation.

# 

# Run Full Pipeline

# .\\scripts\\full\_pipeline.ps1

# Run Health Checks

# .\\scripts\\health\_check.ps1

# Docker Support

# Build Docker Image

# docker build -t sleep-health-analysis .

# Run Docker Container

# docker run sleep-health-analysis

# Continuous Integration

# 

# GitHub Actions automatically runs the pytest suite on:

# 

# pushes

# pull requests

# 

# Workflow configuration:

# 

# .github/workflows/tests.yml

# Outputs \& Artifacts

# 

# The project may generate:

# 

# outputs/

# reports/

# models/

# 

# Potential artifacts include:

# 

# predictions.csv

# test\_results.csv

# cross\_validation\_results.csv

# model\_report.md

# experiment\_metadata.json

# monitoring\_summary.json

# trained model artifacts

# Experiment Tracking

# 

# Experiment metadata includes:

# 

# model name

# metrics

# timestamps

# training row counts

# 

# Tracking utilities are located in:

# 

# src/experiment\_tracker.py

# src/model\_metadata.py

# Monitoring Strategy

# 

# The project includes lightweight monitoring utilities for:

# 

# schema drift

# feature drift

# prediction summaries

# 

# Monitoring documentation:

# 

# docs/monitoring\_plan.md

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

# model card

# artifact strategy

# data dictionary

# Reproducibility

# 

# This project emphasizes reproducibility through:

# 

# pinned package versions

# Docker support

# configuration-driven workflows

# relative file paths

# automated testing

# CI workflows

# Future Improvements

# 

# Potential future enhancements include:

# 

# MLflow integration

# SHAP explainability

# feature importance dashboards

# advanced drift monitoring

# model serving API

# scheduled retraining

# cloud deployment

# Airflow orchestration

# Databricks integration

# Disclaimer

# 

# This repository is intended for educational and machine learning engineering demonstration purposes only.

# 

# The models in this project are not intended for clinical diagnosis or medical decision-making.

