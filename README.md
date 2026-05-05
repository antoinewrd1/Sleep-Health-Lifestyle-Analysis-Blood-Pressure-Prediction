# Sleep-Health-Lifestyle-Analysis-Blood-Pressure-Prediction
This project analyzes the Sleep Health and Lifestyle Dataset to uncover relationships between:  Physical activity Sleep quality Stress levels Cardiovascular health  It combines exploratory data analysis (EDA), visualization, and machine learning to predict systolic blood pressure using real-world lifestyle data.

📂 **Dataset**
Source: Kaggle (Sleep Cycle & Productivity Dataset)
Features include:
Sleep Duration
Quality of Sleep
Physical Activity Level
Stress Level
Heart Rate
Daily Steps
Blood Pressure
Sleep Disorder
⚙️ Tech Stack
Language: Python
Libraries:
Data: pandas
Visualization: matplotlib, seaborn
ML Models: scikit-learn
RandomForestRegressor
SVR
Preprocessing: StandardScaler

🔧 **Project Workflow**
1. Data Loading
Dataset imported using KaggleHub
Loaded into a Pandas DataFrame
2. Data Preparation
Split Blood Pressure into:
Systolic
Diastolic
Applied one-hot encoding for categorical variables
Defined:
Target → Systolic
Features → all other variables (excluding Diastolic)
3. Exploratory Data Analysis (EDA)
Key Insights:
Individuals without sleep disorders have higher daily step counts
Physical activity is associated with:
Longer sleep duration
Lower stress levels
Lower heart rate
4. Regression Visualizations
📈 Daily Steps vs Sleep Duration → Positive relationship
📈 Sleep Duration vs Sleep Quality → Strong positive trend
📉 Physical Activity vs Stress → Negative relationship
📉 Physical Activity vs Heart Rate → Slight negative trend
📈 Age vs Heart Rate → Weak positive trend

🤖 **Machine Learning Models**
🔹 Random Forest Regressor
MSE: 0.2887
R²: 0.9944

✅ Excellent performance
✅ Captures nonlinear relationships
✅ Strong predictive accuracy

🔹 Support Vector Regression (SVR)
MSE: 7.38
R²: 0.8565

⚠️ Lower performance compared to Random Forest
⚠️ Sensitive to scaling and hyperparameters

📊 Model Cparisonom
Model	MSE	R²
Random Forest	0.29	0.99
SVR	7.38	0.86

🏆 Best Model: Random Forest

📈 Feature Importance (Top Predictors)
Heart Rate
Stress Level
Sleep Duration
Physical Activity Level
Age

📌 These align with known physiological drivers of blood pressure.

🔍 **Key Findings**
Increased physical activity leads to:
Better sleep
Lower stress
Improved heart health
Sleep duration strongly impacts sleep quality
Sleep disorders are associated with reduced physical activity
Cardiovascular indicators (heart rate, stress) are strong predictors of blood pressure

▶️ **How to Run**
1. Clone Repository
git clone https://github.com/yourusername/sleep-health-ml.git
cd sleep-health-ml
2. Install Dependencies
pip install pandas matplotlib seaborn scikit-learn kagglehub
3. Run Script
python sleep_analysis.py

📊 **Visual Outputs**
Regression plots
Bar charts (sleep disorder vs activity)
Actual vs Predicted plots
Residual plots
Feature importance chart

🚧 **Future Improvements**
Hyperparameter tuning for SVR (C, gamma, epsilon)
Implement XGBoost / Gradient Boosting
Add cross-validation
Build a dashboard (Streamlit / Tableau)
Deploy model via API (FastAPI)

💼 **Author**

Antoine Ward
Data Scientist | Healthcare Analytics | Machine Learning

GitHub: https://github.com/antoinewrd1
LinkedIn: https://linkedin.com/in/antoine-ward-mph-2401581a1
