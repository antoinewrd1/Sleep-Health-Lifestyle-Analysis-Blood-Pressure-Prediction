import pandas as pd
import streamlit as st

from src.api.main import simple_prediction_rule, PredictionInput


st.set_page_config(
    page_title="Sleep Health BP Predictor",
    layout="wide",
)

st.title("Sleep Health Blood Pressure Prediction Dashboard")

st.write(
    "Interactive dashboard for estimating systolic blood pressure "
    "from sleep and lifestyle factors."
)

age = st.slider("Age", 18, 100, 40)
sleep_duration = st.slider("Sleep Duration", 0.0, 12.0, 7.0)
quality_of_sleep = st.slider("Quality of Sleep", 1, 10, 7)
physical_activity_level = st.slider("Physical Activity Level", 0, 100, 50)
stress_level = st.slider("Stress Level", 1, 10, 5)
heart_rate = st.slider("Heart Rate", 30, 220, 75)
daily_steps = st.slider("Daily Steps", 0, 30000, 7000)

payload = PredictionInput(
    age=age,
    sleep_duration=sleep_duration,
    quality_of_sleep=quality_of_sleep,
    physical_activity_level=physical_activity_level,
    stress_level=stress_level,
    heart_rate=heart_rate,
    daily_steps=daily_steps,
)

prediction = simple_prediction_rule(payload)

st.metric(
    label="Predicted Systolic Blood Pressure",
    value=f"{prediction} mmHg",
)

input_summary = pd.DataFrame(
    [
        {
            "Age": age,
            "Sleep Duration": sleep_duration,
            "Quality of Sleep": quality_of_sleep,
            "Physical Activity Level": physical_activity_level,
            "Stress Level": stress_level,
            "Heart Rate": heart_rate,
            "Daily Steps": daily_steps,
            "Predicted Systolic BP": prediction,
        }
    ]
)

st.subheader("Input Summary")
st.dataframe(input_summary)