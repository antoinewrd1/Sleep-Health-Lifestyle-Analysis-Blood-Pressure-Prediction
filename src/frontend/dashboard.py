import requests
import streamlit as st


API_URL = "http://127.0.0.1:8000"


st.title("Sleep Health BP Admin Dashboard")

api_key = st.text_input("API Key", type="password")

if st.button("Load Admin Summary"):
    response = requests.get(
        f"{API_URL}/admin/summary",
        headers={"x-api-key": api_key},
    )

    if response.status_code == 200:
        st.json(response.json())
    else:
        st.error(response.text)

if st.button("Generate Admin Report"):
    response = requests.post(
        f"{API_URL}/admin/report",
        headers={"x-api-key": api_key},
    )

    if response.status_code == 200:
        st.success("Report generated")
        st.json(response.json())
    else:
        st.error(response.text)