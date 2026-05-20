\# Modeling Decisions



\## Target Variable



The project predicts systolic blood pressure, derived from the original Blood Pressure field.



\## Feature Engineering



The Blood Pressure column is split into:



\- Systolic

\- Diastolic



Sleep Disorder missing values are treated as No Disorder.



\## Models



The project compares:



\- Baseline mean regressor

\- Random Forest Regressor

\- Gradient Boosting Regressor

\- Support Vector Regression



\## Evaluation Metrics



The project uses:



\- MAE

\- RMSE

\- R2



RMSE is used as the primary comparison metric because it penalizes larger prediction errors.

